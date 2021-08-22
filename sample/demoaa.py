# -*- coding: utf-8 -*-
# @Time : 2021/8/13 14:49
# @Author : Limusen
# @File : demoaa

import unittest


class Testa(unittest.TestCase):

    @unittest.skipIf(True, 'dd')
    def test_add(self):
        print('test_add')
        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
