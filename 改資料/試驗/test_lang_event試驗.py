from unittest.case import TestCase
from 改資料.輸出入 import 讀資料


class 單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(讀資料.event換掉(self.原本), self.後來)

    def test_華語前(self):
        self.原本 = '<Event desc="zh" type="language" extent="begin"/>'
        self.後來 = '{'

    def test_華語後(self):
        self.原本 = '<Event desc="zh" type="language" extent="end"/>'
        self.後來 = '}'

    def test_華語無拍instantaneous(self):
        self.原本 = '<Event desc="zh" type="language" extent="instantaneous"/>'
        self.後來 = '{  }'

    def test_華語無拍previous(self):
        self.原本 = '<Event desc="zh" type="language" extent="previous"/>'
        self.後來 = '{  }'

    def test_英語前(self):
        self.原本 = '<Event desc="en" type="language" extent="begin"/>'
        self.後來 = '('

    def test_日語後(self):
        self.原本 = '<Event desc="ja" type="language" extent="end"/>'
        self.後來 = '」'

    def test_別的語言無拍(self):
        self.原本 = '<Event desc="cs" type="language" extent="instantaneous"/>'
        self.後來 = '『  』'
