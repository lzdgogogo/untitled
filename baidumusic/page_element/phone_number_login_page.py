import sys
from baidumusic.utils.log_utils import Logger

logger=Logger()
__author__ = '刘子恒'
from baidumusic.page_element.page_base import page_base
#登录页面-手机号登录页，点击登录会直接跳转到此页面

class phone_login_page(page_base):

        go_to_account_login_button_xpath="//android.view.View[@content-desc=\"账号密码登录\"]"     #去账号密码登录页按钮
        go_to_baidu_login_button_xpath="//android.view.View[@content-desc=\"百度账号登录\"]"       #去百度登录页按钮
        go_to_other_login_button_xpath="//android.view.View[@content-desc=\"其他方式登录\"]"       #其他方式登录按钮

        def is_at_phone_login_page(self):
                """判断是否在此页面"""
                try:
                        if self.driver.find_element_by_xpath(self.go_to_account_login_button_xpath).is_displayed():
                                logger.info(message='在手机号登录页面')
                                return 1
                except:
                        logger.error(message='不在手机号登录页面')
                        return 0


        def go_to_account_login_page(self):
                """点击账号密码登录页按钮，去账号密码登录页"""
                self.driver.find_element_by_xpath(self.go_to_account_login_button_xpath).click()

        def go_to_baidu_login_page(self):
                self.driver.find_element_by_xpath(self.go_to_baidu_login_button_xpath).click()

        def go_to_other_login_page(self):
                self.driver.find_element_by_xpath(self.go_to_other_login_button_xpath).click()