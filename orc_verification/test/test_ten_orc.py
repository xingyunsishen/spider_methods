#!/usr/share/app/anaconda3/bin/python3
# encoding: utf-8  

import unittest

from setting import project_path
from ten_orc import TenOrc


class TestTenOrc(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        self.t_cls = TenOrc()

    def test_orc_start(self):
        file_path = project_path + '/captcha/unit_test/2577.jpg'
        print(self.t_cls.orc_start(file_path=file_path))
        self.assertEqual('2577', (self.t_cls.orc_start(file_path=file_path)))


if __name__ == '__main__':
    unittest.main()
