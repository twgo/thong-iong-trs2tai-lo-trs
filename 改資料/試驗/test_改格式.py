from unittest.case import TestCase
from 改資料.輸出入 import 讀資料


class 單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(讀資料.處理時間(self.原本), self.後來)

    def test_3位以下(self):
        self.原本 = '<Sync time="93.01"/>'
        self.後來 = '<Sync time="93.01"/>'

    def test_3位(self):
        self.原本 = '<Sync time="93.015"/>'
        self.後來 = '<Sync time="93.015"/>'

    def test_3位以上(self):
        self.原本 = '<Sync time="93.0159"/>'
        self.後來 = '<Sync time="93.015"/>'

    def test_float_boundary(self):
        self.原本 = '<Sync time=" 93.015"/>'
        self.後來 = '<Sync time="93.015"/>'

    def test_turn(self):
        self.原本 = '<Turn speaker="spk1" startTime="93.016" endTime="1781.76488">'
        self.後來 = '<Turn speaker="spk1" startTime="93.016" endTime="1781.764">'
