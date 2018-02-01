from os import makedirs, walk
from os.path import dirname, basename, join
import re
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標


class 轉:
    揣音標 = re.compile(r'([a-z]+\d)')

    def __init__(self, 臺羅檔案):
        self.臺羅檔案 = 臺羅檔案

    def 處理(self, 字串):
        錯誤檢查 = re.compile(r'<[^>]+<')
        if 錯誤檢查.search(字串):
            raise ValueError('錯誤')
        切開 = re.compile(r'(<[^>]+>)')
        for 第幾筆, tag in enumerate(切開.split(字串)):
            if 第幾筆 % 2 == 1:
                print(tag, end='', file=self.臺羅檔案)
            else:
                print(
                    self.通用轉臺羅(tag).replace('\n', '\r\n'), end='',
                    file=self.臺羅檔案
                )

    def 通用轉臺羅(self, 聽拍):
        return self.轉外口(self.轉內底(聽拍))

    def 轉外口(self, 聽拍):
        結果 = []
        for 第幾筆, 羅馬字 in enumerate(self.揣音標.split(聽拍)):
            if 第幾筆 % 2 == 0:
                結果.append(羅馬字)
            else:
                臺羅 = 通用拼音音標(羅馬字).轉換到臺灣閩南語羅馬字拼音()
                if 臺羅:
                    結果.append(臺羅)
                else:
                    結果.append(羅馬字)
        return ''.join(結果)

    def 轉內底(self, 聽拍):
        return re.sub(r'(<Event[^/]*type="lexical"[^/]*/>)', self.轉event的lexicon, 聽拍)

    def 轉event的lexicon(self, event):
        tshue = re.split(r'(desc="([a-z]+\d)")', event.group(0))
        臺羅 = 通用拼音音標(tshue[2]).轉換到臺灣閩南語羅馬字拼音()
        if not 臺羅:
            臺羅 = tshue[2]
        結果 = '{}desc="{}"{}'.format(tshue[0], 臺羅, tshue[-1])
        return 結果


if __name__ == '__main__':
    專案 = join(dirname(__file__), '..')
    for 所在, _, 檔名陣列 in walk(join(專案, '分享')):
        for 檔名 in 檔名陣列:
            資料夾名 = basename(所在)
            if 資料夾名 != '臺羅trs' and 檔名.endswith('.trs'):
                通用trs檔名 = join(所在, 檔名)
                臺羅trs檔名 = join(專案, '臺羅', 資料夾名, '臺羅trs', 檔名)
                makedirs(join(dirname(臺羅trs檔名)), exist_ok=True)
                with open(臺羅trs檔名, 'wt') as 臺羅檔案:
                    parser = 轉(臺羅檔案)
                    with open(通用trs檔名, 'rt') as 通用檔案:
                        parser.處理(通用檔案.read())
