from unittest.case import TestCase
from 改資料.輸出入 import 讀資料


class 單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(讀資料.event換掉(self.原本), self.後來)

    def test_正常lexical(self):
        self.原本 = '<Event desc="lor2" type="lexical" extent="previous"/>'
        self.後來 = '[lor2]'
    def test_濟字lexical(self):
        self.原本 = '<Event desc="lor2-lai3" type="lexical" extent="previous"/>'
        self.後來 = '[lor2-lai3]'
    def test_別的符號囥佇lexical(self):
        self.原本 = '<Event desc="silence" type="lexical" extent="instantaneous"/>'
        self.後來 = '[silence]'