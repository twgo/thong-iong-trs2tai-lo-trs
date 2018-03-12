from unittest.case import TestCase
from 轉trs.轉人工 import 轉


class 轉音試驗(TestCase):
    def test_內底(self):
        原本 = '''<Sync time="408.335"/>
di3 e1 gong1 te2-gong1
<Event desc="giong2" type="lexical" extent="previous"/>
-zia4
<Sync time="409.946"/>'''
        後來 = '''<Sync time="408.335"/>
di3 e1 gong1 te2-gong1
<Event desc="kiong7" type="lexical" extent="previous"/>
-zia4
<Sync time="409.946"/>'''
        self.assertEqual(轉('').轉內底(原本), 後來)

    def test_外口(self):
        原本 = '''<Sync time="408.335"/>
zit7-e3 za2-bo2-lang5
<Sync time="409.946"/>'''
        後來 = '''<Sync time="408.335"/>
tsit4-e3 tsa7-poo7-lang5
<Sync time="409.946"/>'''
        self.assertEqual(轉('').轉外口(原本), 後來)
