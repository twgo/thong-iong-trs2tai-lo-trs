from 改資料.輸出入 import 讀資料
from 轉trs.轉人工 import 轉
from http.client import HTTPSConnection
import json
from urllib.parse import quote
import re


class 通用轉漢字臺羅:
    @classmethod
    def trs2trs(cls, 新版本名, 字串, 愛漢字=False):
        for 一筆 in 讀資料.讀(字串):
            if isinstance(一筆, str):
                if 一筆.startswith('<Trans scribe'):
                    yield re.sub('<Trans scribe="(.*?)"', '<Trans scribe="{}"'.format(新版本名), 一筆)
                else:
                    yield 一筆
            else:
                這句 = []
                for 一个 in 一筆:
                    if 一个.startswith('<Event'):
                        這句.append(讀資料.event換掉(一个))
                    else:
                        這句.append(一个)
                原本 = ''.join(這句).strip()
                臺羅 = 轉(None).轉外口(原本)
                切開 = 原本.split('//')
                if len(切開) == 1:
                    華語字幕 = ''
                else:
                    華語字幕 = 切開[0]
                if 愛漢字:
                    yield '漢字：{}'.format(通用轉漢字臺羅.揣漢字(臺羅))
                yield '臺羅：{}'.format(臺羅)
                yield '華語字幕：{}'.format(華語字幕)

    @classmethod
    def 揣漢字(cls, 音標):
        if 音標.strip() == '':
            return ''
        conn = HTTPSConnection("twisas.iis.sinica.edu.tw")
        網址 = (
            "/%E5%8F%A3%E8%AA%9E%E6%A8%99%E6%BC%A2%E5%AD%97%E6%9C%AC%E8%AA%BF/" +
            quote(音標)
        )
        conn.request("GET", 網址)
        r1 = conn.getresponse()
        if r1.status != 200:
            print(網址)
            print(r1.status, r1.reason)
            print(音標)
            raise RuntimeError()
        data1 = r1.read()  # This will return entire content.
        return json.loads(data1.decode('utf-8'))['漢字']


if __name__ == '__main__':
    通用trs檔名 = '分享/Neighbor/NB-twisas/NB-01.trs'
    with open(通用trs檔名, 'rt') as 通用檔案:
        for 一逝 in 通用轉漢字臺羅.trs2trs('sann-pan', 通用檔案.read(), 愛漢字=True):
            print(一逝)
