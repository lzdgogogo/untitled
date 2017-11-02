__author__ = '刘子恒'
#验证太合登录-登出

from baidumusic.page_element.home_mine_page import mine_main
from baidumusic.page_element.phone_number_login_page import phone_login_page
from baidumusic.page_element.account_login_page import account_login_page
from baidumusic import data
from baidumusic.module.test_base import test_base
from baidumusic.page_element.home_music_page import home_page
from baidumusic.page_element.click_more_left_page import click_more_left_page
from baidumusic.page_element.setting_page import setting_page
from baidumusic.page_element.dialog_page import dialog_page
from baidumusic.utils.log_utils import Logger
Logger=Logger()

class TaiheLoginLogout(test_base):
        def after_login(self):
                """功能：
                        在登录之前做的准备工作,从启动app--我的页--判断登录态--进入手机号登录页
                返回值：
                        1：已经在登录态了，需要先退出登录
                        2：在非登陆态可以继续测试"""
                cur_homepage=home_page(self.driver)                                             #进入我的页
                cur_homepage.go_to_mine_page()

                cur_minepage=mine_main(self.driver)
                self.wait_driver_by_id(5,cur_minepage.down_load_music_id,'进入我的页')
                self.screenshot('登录功能——我的页截图')
                if cur_minepage.is_unlogin() == 1:                                               #判断是否在登录态
                        return 1


                cur_minepage.go_to_phone_number_login_page()                                   #进入手机号登录页
                self.my_sleep(2)

        def taihe_login(self):
                """功能：
                        太合登录的主过程：手机号登录页--账号密码登录页--输入账号密码--检查登录情况
                返回值：
                        1：登录成功
                        -1：登录失败"""

                cur_phone_login_page = phone_login_page(self.driver)
                if not cur_phone_login_page.is_at_phone_login_page():
                        self.tear_down()
                self.screenshot('手机号登录页截图')

                cur_phone_login_page.go_to_account_login_page()                                 #进入账号密码登录页
                self.my_sleep(3)
                cur_account_login_page=account_login_page(self.driver)
                if cur_account_login_page.is_at_account_login_page() == 1:
                        Logger.info(message='进入账号密码登录页成功')
                else:
                        Logger.error(message='进入账号密码登录页失败')
                        self.tear_down()

                cur_account_login_page.input_account(data.TAIHE_PHONE_NUMBER)
                cur_account_login_page.input_password(data.TAIHE_PASSWORD)
                cur_account_login_page.click_login_button()                                     #点击后会自动跳转到我的页

                cur_minepage=mine_main(self.driver)
                if cur_minepage.is_unlogin() == 1:
                        return 1
                else:
                        return -1

        def sign_out(self):
                """执行退出登录
                返回值：
                        1：测试成功
                        -1：在非登录态，需要先去登陆才可以继续测试
                        -2：登出失败"""

                self.my_sleep()
                cur_homepage=home_page(self.driver)
                cur_homepage.click_more_button()        #点击更多按钮
                Logger.info(message='点击更多按钮')
                self.my_sleep()

                cur_left_page=click_more_left_page(self.driver)
                if cur_left_page.is_login() == -1:                      #判断是否在登录态
                        Logger.error(message='当前在非登录态，先去登陆！')

                        self.screenshot('登出功能——非登录状态截图')
                        self.reset_app()
                        self.test_taihe_login()
                        self.reset_app()
                        cur_homepage=home_page(self.driver)
                        cur_homepage.click_more_button()        #点击更多按钮
                        Logger.info(message='点击更多按钮')
                        self.my_sleep()

                self.screenshot('登出功能——登录状态截图')
                cur_left_page.click_setting_container()
                Logger.info(message='点击设置按钮')
                self.my_sleep()

                cur_settting_page=setting_page(self.driver)
                cur_settting_page.click_signout_button()        #点击退出按钮
                Logger.info(message='点击退出按钮')
                self.my_sleep(2)

                cur_dialog_page=dialog_page(self.driver)
                cur_dialog_page.click_yes_button()              #点击退出登录
                Logger.info(message='点击退出登录')
                self.my_sleep()

                cur_homepage.click_more_button()                #点击更多按钮查看登录态
                Logger.info(message='查看登录态')
                if cur_left_page.is_login() == 1:
                        return -2
                return 1

        def test_sign_out(self):
                """功能：
                        测试登出功能"""
                self.wait_start_app()
                Logger.info(message='开始测试登出功能')

                if self.sign_out() == -2:
                        Logger.war(message='当前还在登录状态！登出失败!')
                        self.screenshot('登出功能——登出失败截图')
                else:
                        Logger.info(message='登出成功')
                        self.screenshot('登出功能——登出成功截图')

        def test_taihe_login(self):
                """功能：
                        测试登录功能"""
                self.wait_start_app()
                Logger.info(message='开始测试登录功能')
                if self.after_login() == 1:
                        Logger.war(message='已经在登录态了!需要先退出登录')
                        self.reset_app()
                        self.test_sign_out()

                        if self.after_login() == 1:
                                Logger.error(message='异常情况！退出测试')
                                self.tear_down()

                if self.taihe_login() == 1:
                        Logger.info(message='登陆成功')
                        self.screenshot('登录功能——登录成功截图')
                else:
                        Logger.error(message='登录失败')
                        self.screenshot('登录功能——登录失败截图')




