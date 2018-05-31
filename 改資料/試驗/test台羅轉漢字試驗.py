from unittest.case import TestCase
from unittest.mock import call, patch
from 輸出入 import 通用轉漢字臺羅


class 單元試驗(TestCase):
    @patch('輸出入.通用轉漢字臺羅.twisas揣漢字')
    def test_內容(self, twisas揣漢字mock):
        羅馬字 = 'sann1 e5 {中國人} tsuá--lai5'
        通用轉漢字臺羅.揣漢字(羅馬字)
        twisas揣漢字mock.assert_has_calls([
            call('sann1 e5 '),
            call(' tsuá--lai5'),
        ])