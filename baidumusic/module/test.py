from selenium.webdriver.common.by import By
import sys
from baidumusic.module.test_base import test_base
from baidumusic.page_element.home_mine_page import home_mine_page
from baidumusic.page_element.home_music_page import home_music_page
from baidumusic.page_element.phone_number_login_page import phone_number_login_page

__author__ = '刘子恒'

class test(test_base):
        def test(self):
                self.wait_start_app()
                self.my_sleep()


                #self.is_element_display(By.XPATH,'//android.widget.GridView[@resource-id=\"com.ting.mp3.android:id/gridview\"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]','首页控件')
                #if self.is_element_display(By.ID,'com.ting.mp3.android:id/day_tv','首页控件') == -1:
                        #sys.exit()

                #if self.find_element_and_click(By.ID,'com.ting.mp3.android:id/day_tv') == -1:   sys.exit()
                #if self.find_element_and_click(By.XPATH,'//android.widget.GridView[@resource-id=\"com.ting.mp3.android:id/gridview\"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]') == -1:   sys.exit()

                cur_music_page=home_music_page(self.driver)
                cur_music_page.go_to_mine_page()
                self.my_sleep()
                cur_mine_page=home_mine_page(self.driver)
                cur_mine_page.go_to_phone_number_login_page()

                cur_phone_number_login_page=phone_number_login_page(self.driver)
                self.wait_element_by_mode(15,By.XPATH,cur_phone_number_login_page.go_to_account_login_button_xpath,'进入手机号登录页')


                self.my_sleep(3)
                self.tear_down()
