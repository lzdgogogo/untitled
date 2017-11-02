#encoding:utf8
#!/usr/bin/env python

import datetime
import logging
import os
import sys

TIME=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

root_dir = '/'.join(os.path.realpath(__file__).split('\\')[:-1])
root_dir = os.path.dirname(root_dir) + os.path.sep
sys.path.append(root_dir)

logLevel = 2
#logFile = os.path.join(root_dir, 'logs')
logFile = os.path.abspath(os.getcwd()+'/logs'+'/')

logLevel_list = {
      1 : logging.NOTSET,
      2 : logging.DEBUG,
      3 : logging.INFO,
      4 : logging.WARNING,
      5 : logging.ERROR,
      6 : logging.CRITICAL
}

g_loggers = {}

#  定义日志方法,从配置文件读取日志等级,且定义日志输出路径
file_extension = '.log'



class Logger:
    def __init__(self):
        self.log_level = logLevel
        log_path = logFile
        self.log_file = os.path.join(log_path, TIME + file_extension)
        self._fileExist()

    def _fileExist(self):
        temp_path=os.path.abspath(os.getcwd()+'/logs'+'/')
        if not os.path.isdir(temp_path):
                      os.makedirs(temp_path)

    def _loggers(self,**kwargs):
        global g_loggers
        self._fileExist()
        logger = logging.getLogger('logger')
        #设置log级别
        log_level = self.log_level
        log_file = self.log_file
        logger.setLevel(logLevel_list[log_level])
        if not logger.handlers:
            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(log_file)
            fh.setLevel(logLevel_list[log_level])
            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            fh.setFormatter(formatter)
            # 再创建一个handler，用于输出到控制台

            ch = logging.StreamHandler()
            ch.setLevel(logLevel_list[log_level])
            ch.setFormatter(formatter)
            logger.addHandler(ch)
            # 给logger添加handler
            logger.addHandler(fh)
            g_loggers.update(dict(name=logger))
        return  logger

    def debug(self,message):
        self._loggers().debug(message)
    def info(self,message):
        self._loggers().info(message)
    def war(self,message):
        self._loggers().warn(message)
    def error(self,message):
        self._loggers().error(message)
    def cri(self,message):
        self._loggers().critical(message)




