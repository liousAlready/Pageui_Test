# -*- coding: utf-8 -*-
# @Time : 2021/8/3 16:08
# @Author : Limusen
# @File : test_demo


import unittest


class TestA(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.a = 1
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:  # 类级别的
        print("tearDownClass")

    def setUp(self) -> None:  # 方法级别的
        print("setUp %d"% self.a)

    def tearDown(self) -> None:
        print("tearDown")

    def test_01(self):
        print("test0 %d"% self.a)
        self.assertTrue(True)

    def test_02(self):
        print("test01")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
