from selenium.common.exceptions import NoSuchElementException

__author__ = '刘子恒'
#主页的我的目录下       这个页面在登录态和非登录态会有区别
from baidumusic.page_element.home_page import home_page

class mine_main(home_page):

        #上边栏
        more_button_id='com.ting.mp3.android:id/more'                        #更多
        skin_button_id='com.ting.mp3.android:id/skin'                        #皮肤
        message_button_id='com.ting.mp3.android:id/message'                  #信息
        setting_button_id='com.ting.mp3.android:id/Setting_btn'              #设置

        #用户信息栏  在登录态和非登录态会有区别
        #登录态
        login_user_img_id='com.ting.mp3.android:id/user_img'                 #用户头像
        login_user_name_id='com.ting.mp3.android:id/loginName'               #用户名
        #非登录态
        unlogin_user_img_id='com.ting.mp3.android:id/user_img_unlogin'       #非登录态用户头像框
        unlogin_container_id='com.ting.mp3.android:id/container_unlogin'     #用户非登录布局（点击这里可以进入登录页面）


        #离线缓存、最近播放、缓存管理
        local_music_id='com.ting.mp3.android:id/container_local_music'       #离线缓存
        play_history_id='com.ting.mp3.android:id/container_playhistory'      #最近播放
        down_load_music_id='com.ting.mp3.android:id/container_downloadmusic' #缓存管理


        def go_to_phone_number_login_page(self):
                self.driver.find_element_by_id(self.unlogin_container_id).click()

        def is_unlogin(self):
                """判断是否在登录态
                返回值：
                        1：在登录态
                        2：在非登录态
                """
                try:
                        if self.driver.find_element_by_id(self.unlogin_container_id).is_displayed():
                                return 2

                except NoSuchElementException:
                        if self.driver.find_element_by_id(self.login_user_img_id).is_displayed():
                                return 1

