import sys
from baidumusic.utils.log_utils import Logger

logger=Logger()
__author__ = '刘子恒'
from baidumusic.page_element.page_base import page_base
#登录页面-手机号

class BaiduLoginPage(page_base):

        user_name_input_bar_xpath = "//android.widget.EditText[@resource-id=\"login-username\"]"        #百度用户名输入栏
        password_input_bar_xpath = "//android.widget.EditText[@resource-id=\"login-password\"]"         #密码输入栏
        login_button_xpath = "//android.widget.Button[@resource-id=\"login-submit\"]"                   #登录按钮
        log_containers_xpath = "//android.view.View[@resource-id=\"login\"]/android.view.View[2]"       #百度log


        # def is_at_baidu_login_page(self):
        #         """功能：
        #                 判断是否在此页面
        #         参数：
        #                 1：在百度登录页面
        #                 0：不在"""
        #         try:
        #                 if self.driver.find_element_by_xpath(self.log_containers_xpath).is_displayed():
        #                         logger.info(message='在百度登录页面')
        #                         return 1
        #         except:
        #                 logger.error(message='不在百度登录页面')
        #                 return 0

        def click_login_button(self):
                """功能：
                        点击登录按钮"""
                self.driver.find_element_by_xpath(self.login_button_xpath).click()
                logger.info(message='点击登录按钮')

        def input_account(self,account=''):
                """输入账号
                参数：账号"""
                self.driver.find_element_by_xpath(self.user_name_input_bar_xpath).send_keys(account)

        def input_password(self,password=''):
                """输入密码
                参数：密码"""
                self.driver.find_element_by_xpath(self.password_input_bar_xpath).send_keys(password)