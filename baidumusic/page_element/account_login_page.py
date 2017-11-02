from selenium.common.exceptions import NoSuchElementException

__author__ = '刘子恒'
#登录页面-账号密码登录页
from baidumusic.page_element.page_base import page_base

class account_login_page(page_base):

        account_input_bar_xpath="//android.webkit.WebView/android.view.View[4]/android.widget.EditText"        #账号栏
        password_input_bar_xpath="//android.webkit.WebView/android.view.View[5]/android.widget.EditText"         #密码栏
        login_button_xpath="//android.webkit.WebView/android.view.View[6]/android.widget.Button"               #登录按钮
        account_login_log_xpath="//android.view.View[@content-desc=\"太合账号登录\"]"      #账号登录文字栏logo 可用来验证有没有在此页面

        def is_at_account_login_page(self):
                """判断当前是不是在账号密码登录页
                        返回值：1 在账号密码登录页
                                -1 不在"""
                try:
                        if self.driver.find_element_by_xpath(self.account_login_log_xpath).is_displayed():
                                return 1
                except NoSuchElementException:
                        return -1


        def click_login_button(self):
                """点击登录按钮"""
                self.driver.find_element_by_xpath(self.login_button_xpath).click()
                
        def input_account(self,account=''):
                """输入账号
                参数：账号"""
                self.driver.find_element_by_xpath(self.account_input_bar_xpath).send_keys(account)

        def input_password(self,password=''):
                """输入密码
                参数：密码"""
                self.driver.find_element_by_xpath(self.password_input_bar_xpath).send_keys(password)

