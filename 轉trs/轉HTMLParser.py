
from html.parser import HTMLParser


class TrsParser(HTMLParser):
    def __init__(self, 臺羅檔案):
        super().__init__()
        self.臺羅檔案 = 臺羅檔案

    def handle_starttag(self, tag, attrs):
        輸出 = '<{} {}>'
        屬性 = ' '.join(['{}={}'.format(attr[0], attr[1]) for attr in attrs])
        print("Encountered a start tag:", 輸出.format(tag, 屬性))
        print(輸出.format(tag, 屬性), end='', file=self.臺羅檔案)

    def handle_endtag(self, tag):
        輸出 = '<{}/>'
        print("Encountered an end tag :", 輸出.format(tag))
        print(輸出.format(tag), end='', file=self.臺羅檔案)

    def handle_data(self, data):
        print(data, end='', file=self.臺羅檔案)


通用trs檔名 = '/home/ciciw/git/Ko_corpus/Finished/ALen&Tea/ALan&Tea_001(ChangNeng).trs'
臺羅trs檔名 = 'a.trs'
with open(臺羅trs檔名, 'wt') as 臺羅檔案:
    parser = TrsParser(臺羅檔案)
    with open(通用trs檔名, 'rt') as 通用檔案:
        parser.feed(通用檔案.read())
