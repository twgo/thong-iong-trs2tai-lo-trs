import re


class 讀資料:
    @classmethod
    def 讀(cls, 檔案資料):
        結果 = []
        for 一逝 in 檔案資料.strip().replace('\r\n', '\n').split('\n'):
            if cls.是資料(一逝):
                try:
                    結果[-1].append(一逝)
                except AttributeError:
                    結果.append([一逝])
            else:
                結果.append(一逝)
        return 結果

    @classmethod
    def 是資料(cls, 一逝):
        if not 一逝.startswith('<'):
            return True
        if 一逝.startswith('<Event'):
            return True
        return False

    @classmethod
    def event換掉(cls, 一逝):
        拍毋著字 = {
            'silencd': 'silence',
            'sile3nce': 'silence',
            'sience': 'silence',
            'silecne': 'silence',
            'noisy': 'noise',
            'silecne': 'noise',
            'nooise': 'noise',
            'npoise': 'noise',
            'emtpy': 'empty',
            'emty': 'empty',
        }
        if 'type="noise"' in 一逝:
            型態 = re.search('desc="(.+?)"', 一逝).group(1)
            if 型態 in 拍毋著字:
                型態 = 拍毋著字[型態]
            return ' {} '.format(型態.upper())
