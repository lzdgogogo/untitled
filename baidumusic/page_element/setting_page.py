__author__ = '刘子恒'
from baidumusic.page_element.page_base import page_base

#设置页面，通过点击设置按钮来进入，可以在这里查看版本和退出登录等

#点击退出后会弹出：关闭百度音乐和退出登录两个选项，也放在此页

class setting_page(page_base):
        signout_button_id = 'com.ting.mp3.android:id/bt_logout'         #退出按钮

        logout_layout_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/dialog_list\"]\
                                /android.widget.RelativeLayout[2]"                                        #点击退出按钮后弹出的退出登录布局


        def click_signout_button(self):
                """功能：
                        点击退出按钮，退出按钮在页面底部，所以要先将页面滑到底部再点击。之后再弹出的底部栏，点击退出登录"""
                self.my_sleep()
                self.swipe_up()
                self.my_sleep()

                self.try_find_element_by_id_click(self.signout_button_id)
                self.my_sleep()
                self.driver.find_element_by_xpath(self.logout_layout_xpath).click()
