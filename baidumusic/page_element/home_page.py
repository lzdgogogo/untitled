__author__ = '刘子恒'
#百度音乐APP首页，在这个页面中，左上角更多按钮、minibar、下边栏是一直显示的。
from baidumusic.page_element.page_base import page_base

class home_page(page_base):
        #这些都是主页的共同部分

        more_button_id='com.ting.mp3.android:id/more_layout'                        #左上角更多按钮

        #minibar
        minibar_song_name_id='com.ting.mp3.android:id/mb_text_trackname'            #minibar中歌名
        minibar_singer_name_id='com.ting.mp3.android:id/mb_text_artist'             #歌手名
        minibar_control_button_id='com.ting.mp3.android:id/mb_control'              #播放按钮
        minibar_next_button_id='com.ting.mp3.android:id/mb_next'                    #下一首按钮
        minibar_playlist_button_id='com.ting.mp3.android:id/mb_list'                #列表按钮
        #下边栏
        i_music_id='com.ting.mp3.android:id/i_music'                                 #音乐
        i_anylisten_id='com.ting.mp3.android:id/i_anylisten'                         #随心听
        i_trends_id='com.ting.mp3.android:id/i_trends'                               #动态
        i_mine_id='com.ting.mp3.android:id/i_mine'                                    #我的

        def click_more_button(self):
                """功能：
                        点击更多按钮"""
                self.driver.find_element_by_id(self.more_button_id).click()

        def go_to_mine_page(self):
                """功能：
                        点击我的按钮"""
                self.driver.find_element_by_id(self.i_mine_id).click()

        def go_to_music_page(self):
                """功能：
                        点击音乐按钮"""
                self.driver.find_element_by_id(self.i_music_id).click()
