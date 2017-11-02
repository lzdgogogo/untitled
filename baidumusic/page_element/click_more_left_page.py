__author__ = '刘子恒'
#点击了主页上的more按钮后从左边弹出来的按钮
from baidumusic.page_element.page_base import page_base
from selenium.common.exceptions import NoSuchElementException

class click_more_left_page(page_base):
        user_img_id = 'com.ting.mp3.android:id/user_img'                        #登陆后的用户头像
        go_login_button_id = 'com.ting.mp3.android:id/go_login'                 #在非登陆态的立即登录

        setting_container_id = 'com.ting.mp3.android:id/setting_container'      #设定按钮容器

        def click_setting_container(self):
                """功能：
                        点击设置来进入设置页面"""
                self.driver.find_element_by_id(self.setting_container_id).click()

        def is_login(self):
                """功能：
                        检查是否在登录态，假如在登录态返回1，非登录态返回-1"""

                try:
                        if self.driver.find_element_by_id(self.go_login_button_id).is_displayed():
                                return -1
                except NoSuchElementException:
                        return 1

