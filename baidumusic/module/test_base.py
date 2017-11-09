from selenium.common.exceptions import NoSuchElementException

__author__ = '刘子恒'
import unittest
import os
import time
from appium import webdriver
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from baidumusic.utils.log_utils import Logger

Logger=Logger()

# noinspection PyArgumentList
class test_base(object):

        TIME=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))#脚本开始时间
        PATH = lambda p: os.path.abspath(p)
        def __init__(self):
                """功能：
                        初始化drier"""
                Logger.info(message='测试开始')
                #self.print_log('测试开始')
                desired_caps={}
                desired_caps['platformName']='Android'
                desired_caps['platformVersion']='5.0'
                desired_caps['deviceName']='123'
                desired_caps['appPackage']='com.ting.mp3.android'
                desired_caps['appActivity']='com.baidu.music.ui.splash.SplashActivity'
                self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

        def tear_down(self):
                """功能：
                        关闭APP，driver退出，结束测试"""
                self.driver.close_app()
                self.driver.quit()
                Logger.info(message='测试结束')
                #self.print_log('测试结束')
                sys.exit()


        @staticmethod
        def my_sleep(t=1):
                """功能：
                        程序睡眠t秒"""
                time.sleep(t)

        number=1
        def screenshot(self,des):
                """功能：
                        截屏
                参数：
                        截图描述，为一个字符串"""

                temp_path=os.path.abspath(os.getcwd()+'/screenshot'+'/'+self.TIME)


                if not os.path.isdir(temp_path):
                      os.makedirs(temp_path)
                self.driver.get_screenshot_as_file(temp_path+'/'+'%d'%self.number+'.'+des+'.png')
                self.number += 1

        def wait_element_by_mode(self,t,mode,element_id,thing=''):
                """功能：
                        设置等待的函数。
                参数：
                        t:是最长等待时间。
                        mode:查找模式，例如：By.ID,By.XPATH
                        element:等待的元素查找依据，比如id,xpath，应该与mode的模式相匹配。
                        thing：等待的元素的描述，应该为字符串"""
                try:
                        WebDriverWait(self.driver,t).until(expected_conditions.presence_of_element_located((mode,element_id)))
                except NoSuchElementException:
                        Logger.error(message=thing+'超时')
                        #self.print_log(thing+'超时')
                        self.screenshot(thing+'等待超时截图')
                        self.driver.quit()
                        sys.exit(-1)
                Logger.info(message=thing+'成功')
                #self.print_log(thing+'成功')

        def get_size(self):
                """功能：
                        获取本机的分辨率，返回值是屏幕的长和宽"""
                x=self.driver.get_window_size()['width']
                y=self.driver.get_window_size()['height']
                return x,y

        def swipe_up(self,t,x=0.5):
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

        def reset_app(self):
                """功能：
                        重启APP,并且等待app重新启动完成"""
                self.driver.close_app()
                self.driver.launch_app()
                self.wait_element_by_mode(15,By.ID,'com.ting.mp3.android:id/vp','重启APP')

        def wait_start_app(self):
                """功能：
                        等待app启动,并且截图"""

                self.wait_element_by_mode(15,By.ID,'com.ting.mp3.android:id/bubble','启动APP')
                self.screenshot('启动APP截图')


        def my_find_element_by_id(self,element_id):
                """功能：
                        通过id查找控件，不一样的地方是做了异常处理，当找不到控件的时候会打印日志并且截图，关闭driver，程序退出
                参数：
                        要查找的控件的id"""
                try:
                        self.driver.find_element_by_id(element_id)
                except NoSuchElementException:
                        Logger.error(message='当前所要查找控件在当前页面不能被找到')
                        #self.print_log('当前所要查找控件在当前页面不能被找到')
                        self.screenshot('查找不到控件页面截图')
                        self.driver.quit()
                        sys.exit(-1)


        def click_wait_by_id(self,element_id,t=1):
                """功能：
                        通过ID查找一个控件并点击，然后睡眠t秒，默认为1秒

                参数：
                        element_id是要查找并点击的控件的id，必须为字符串，
                        t为点击后睡眠的时间，默认为一秒"""
                self.driver.find_element_by_id(element_id).click()
                self.my_sleep(t)

        def click_wait_by_xpath(self,xpath,t=1):
                """功能：
                        通过xpath查找一个控件并点击，然后睡眠t秒，默认为1秒
                参数：
                        xpath是要查找的控件的xpath，
                        t为点击后睡眠的时间，默认为一秒"""
                self.driver.find_element_by_xpath(xpath).click()
                self.my_sleep(t)

        def is_element_display(self,mode,element='',thing=''):
                """功能：
                        判断控件是否显示在当前页面上
                参数：
                        mode：以哪种方式寻找控件，必须是以下几种:By.ID, By.CLASS_NAME, By.XPATH, By.NAME
                        element：控件的id或者xpath等，要跟前一项对应，
                        thing：描述"""
                try:
                        if self.driver.find_element(mode,element).is_displayed():
                                Logger.info(message=thing+'显示')
                                #log_utils.C_INFO(thing+'显示')
                                return 1
                        else:
                                Logger.error(message=thing+'未显示')
                                #log_utils.F_ERROR(thing+'未显示')
                                return 0
                except:
                        Logger.error(message=thing+'不在当前页面')
                        # log_utils.F_ERROR(thing+'不在当前页面')
                        return -1

        def find_element_and_click(self,mode,element='',thing=''):
                """功能：
                        以某种方式查找控件并且点击，但是保证不会因为找不到控件而跳出
                参数：
                        mode：以哪种方式寻找控件，必须是以下几种:By.ID, By.CLASS_NAME, By.XPATH, By.NAME
                        element：控件的id或者xpath等，要跟前一项对应，
                        thing：描述
                返回值：
                        1：点击成功
                        -1：控件不在当前页面"""
                try:
                        self.driver.find_element(mode,element).click()
                        Logger.info(message='点击'+thing)
                        return 1
                except:
                        Logger.error(message=thing+'不在当前页面')
                        return -1



























        # def print_log(self,thing):
        #         """功能：
        #                 输出一个美观一点的信息
        #         参数：
        #                 要输出的信息，应该为一个字符串"""
        #         print('------------------------- '+thing+' ----------------------------------')



