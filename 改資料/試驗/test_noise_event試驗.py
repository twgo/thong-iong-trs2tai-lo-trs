from unittest.case import TestCase
from 改資料.輸出入 import 讀資料


class 單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(讀資料.event換掉(self.原本), self.後來)

    def test_符號改大寫(self):
        self.原本 = '<Event desc="mix" type="noise" extent="instantaneous"/>'
        self.後來 = ' MIX '

    def test_華語後(self):
        self.原本 = '<Event desc="noise" type="noise" extent="instantaneous"/>'
        self.後來 = ' NOISE '

    def test_previous無要緊(self):
        self.原本 = '<Event desc="silence" type="noise" extent="previous"/>'
        self.後來 = ' SILENCE '

    def test_拍毋著詞替伊改(self):
        self.原本 = '<Event desc="silencd" type="noise" extent="instantaneous"/>'
        self.後來 = ' SILENCE '
