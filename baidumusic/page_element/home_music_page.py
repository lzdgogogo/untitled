__author__ = '刘子恒'
#主页的音乐目录下
from baidumusic.page_element.home_page import home_page

class home_music_page(home_page):

        #上边栏
        search_layout_id='com.ting.mp3.android:id/search_layout',             #搜索栏
        #搜索栏下方栏
        recommend_xpath="//android.widget.HorizontalScrollView[@resource-id=\"com.ting.mp3.android:id/tabsLayout\"]\
                                /android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]",      #搜索栏下方推荐按钮
        song_list_xpath="//android.widget.LinearLayout/android.widget.TextView[2]",                                     #歌单



