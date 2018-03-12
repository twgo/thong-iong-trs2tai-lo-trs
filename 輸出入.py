from 改資料.輸出入 import 讀資料
from 轉trs.轉人工 import 轉


if __name__ == '__main__':
    通用trs檔名 = '分享/Neighbor/NB-twisas/NB-01.trs'
    with open(通用trs檔名, 'rt') as 通用檔案:
        for 一筆 in 讀資料.讀(通用檔案.read()):
            if isinstance(一筆, str):
                print(一筆)
            else:
                這句=[]
                for 一个 in 一筆:
                    if 一个.startswith('<Event'):
                        這句.append(讀資料.event換掉(一个))
                    else:
                        這句.append(一个)
                原本=''.join(這句).strip()
                通用=原本
                print('漢字：{}'.format(原本))
                print('臺羅：{}'.format(轉(None).轉外口(原本)))
                print('通用：{}'.format(原本))
                print('原本：{}'.format(原本))
