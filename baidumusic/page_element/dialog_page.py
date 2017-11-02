__author__ = '刘子恒'
from baidumusic.page_element.page_base import page_base
#例如在点击退出登录、删除歌单时，弹出的窗口

class dialog_page(page_base):

        yes_button_id = 'com.ting.mp3.android:id/dialog_common_confirm'
        cancel_button_id = 'com.ting.mp3.android:id/dialog_common_cancel'


        def click_yes_button(self):
                """点击确定（此按钮一直在右边）"""
                self.try_find_element_by_id_click(self.yes_button_id)

        def click_cancel_button(self):
                """点击取消（此按钮在左边）"""
                self.try_find_element_by_id_click(self.cancel_button_id)