from unittest.case import TestCase
from 輸出入介面 import 通用轉漢字臺羅


class 單元試驗(TestCase):

    def tearDown(self):
        self.assertEqual(通用轉漢字臺羅.分台華(self.原來), self.答案)

    def test_純通用(self):
        self.原來 = 'oh2 li1 siunn3 kuann4 mai2 li1 na3 hun2-pue4 ki1 lai3-kim5 e2'
        self.答案 = 'oh2 li1 siunn3 kuann4 mai2 li1 na3 hun2-pue4 ki1 lai3-kim5 e2', ''

    def test_頭前有華語(self):
        self.原來 = '我看你才是丈人看女婿//ah1 qua1 kuann3 oh3 ,li1 ziah1-si3'
        self.答案 = 'ah1 qua1 kuann3 oh3 ,li1 ziah1-si3', '我看你才是丈人看女婿'

    def test_華語佇後壁標(self):
        self.原來 = 'iah1-m3-gorh1 li1 ing4-gai2 ga3 qua1 gong4 zit3 siann3 可是你應該告訴我一聲//'
        self.答案 = 'iah1-m3-gorh1 li1 ing4-gai2 ga3 qua1 gong4 zit3 siann3', '可是你應該告訴我一聲'

    def test_華語佇後壁有空白(self):
        self.原來 = 'iah1-m3-gorh1 li1 ing4-gai2 ga3 qua1 gong4 zit3 siann3 可是你 應該告訴我一聲//'
        self.答案 = 'iah1-m3-gorh1 li1 ing4-gai2 ga3 qua1 gong4 zit3 siann3', '可是你 應該告訴我一聲'

    def test_全漢字閣刪節號(self):
        self.原來 = '來了...//'
        self.答案 = '', '來了...'
