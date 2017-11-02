__author__ = '刘子恒'

from baidumusic.module.taihe_login_logout import taihe_login_logout


if __name__ == '__main__':
        my_test=taihe_login_logout()

        my_test.test_sign_out()

        my_test.tear_down()
