import sys
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from baidumusic.utils.log_utils import Logger

Logger=Logger()

__author__ = '刘子恒'
class page_base(object):
        def __init__(self,drivers):
                self.driver=drivers

        def tear_down(self):
                """功能：
                        关闭APP，driver退出，结束测试"""
                self.driver.close_app()
                self.driver.quit()
                Logger.info(message='测试结束')
                sys.exit()

        def get_size(self):
                """功能：
                        获取本机的分辨率，返回值是屏幕的长和宽"""
                x=self.driver.get_window_size()['width']
                y=self.driver.get_window_size()['height']
                return x,y

        def swipe_up(self,t=500,x=0.5):
                """功能：
                        屏幕向上滑动。
                参数：
                        t是滑动的时间，t越小代表滑的越快，滑的距离越大,t的单位是毫秒。
                        x是向上滑动时手指在屏幕的横向位置，
                        例如x=0.5，手指就在屏幕中间向下滑，x=0.25，就在屏幕四分之一的地方向下滑"""
                size=self.get_size()
                x1=int(size[0]*x)
                y1=int(size[1]*0.75)
                y2=int(size[1]*0.25)
                self.driver.swipe(x1,y1,x1,y2,t)

        # def print_log(self,thing=''):
        #         """功能：
        #                 输出一个美观一点的信息
        #         参数：
        #                 要输出的信息，应该为一个字符串"""
        #         print('------------------------- '+thing+' ----------------------------------')

        def my_find_element_by_id(self,element_id):
                """功能：
                        通过id查找控件，不一样的地方是做了异常处理，当找不到控件的时候会打印日志并且截图，关闭driver，程序退出
                参数：
                        要查找的控件的id"""
                try:
                        self.driver.find_element_by_id(element_id)
                except NoSuchElementException:
                        Logger.error(message='当前所要查找控件在当前页面不能被找到')
                        self.driver.quit()
                        sys.exit(-1)

        def my_find_element_by_xpath(self,element_xpath):
                """功能：
                        通过xpath查找控件，不一样的地方是做了异常处理，当找不到控件的时候会打印日志并且截图，关闭driver，程序退出
                参数：
                        要查找的控件的id"""
                try:
                        self.driver.find_element_by_xpath(element_xpath)
                except NoSuchElementException:
                        Logger.error(message='当前所要查找控件在当前页面不能被找到')
                        self.driver.quit()
                        sys.exit(-1)

        def try_find_element_by_id_click(self,element_id):
                """功能：
                        通过id查找控件并且点击"""
                try:
                        self.driver.find_element_by_id(element_id).click()
                except NoSuchElementException:
                        Logger.error(message='当前所要查找控件在当前页面不能被找到')
                        self.driver.quit()
                        sys.exit(-1)

        @staticmethod
        def my_sleep(t=1):
                """功能：
                        程序睡眠t秒"""
                time.sleep(t)