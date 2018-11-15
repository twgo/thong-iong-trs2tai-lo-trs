from unittest.case import TestCase
from unittest.mock import call, patch
from 輸出入介面 import 通用轉漢字臺羅


class 單元試驗(TestCase):
    @patch('輸出入介面.通用轉漢字臺羅.twisas揣漢字')
    def test_內容(self, twisas揣漢字mock):
        twisas揣漢字mock.return_value = ''
        羅馬字 = 'sann1 e5 {中國人} tsuá--lai5'
        通用轉漢字臺羅.揣漢字(羅馬字)
        twisas揣漢字mock.assert_has_calls([
            call('sann1 e5 '),
            call(' tsuá--lai5'),
        ])

    @patch('輸出入介面.通用轉漢字臺羅.twisas揣漢字')
    def test_內容2(self, twisas揣漢字mock):
        twisas揣漢字mock.return_value = ''
        羅馬字 = 'ao1-i2-ui2-{三民主義}-lai3-te2,leh8-kong1-bin7-tsok4-tsu1-gi7-honnh4-'
        通用轉漢字臺羅.揣漢字(羅馬字)
        twisas揣漢字mock.assert_has_calls([
            call('ao1-i2-ui2-'),
            call('-lai3-te2,leh8-kong1-bin7-tsok4-tsu1-gi7-honnh4-'),
        ])
