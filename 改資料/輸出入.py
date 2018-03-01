
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
