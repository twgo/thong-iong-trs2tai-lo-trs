from unittest.case import TestCase
from 改資料.輸出入 import 讀資料


class 單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(讀資料.讀(self.原本), self.後來)

    def test_內容(self):
        self.原本 = '''<Sync time="408.335"/>
di3 e1 gong1 te2-gong1
<Event desc="giong2" type="lexical" extent="previous"/>
-zia4
<Sync time="409.946"/>'''
        self.後來 = [
            '<Sync time="408.335"/>',
            [
                'di3 e1 gong1 te2-gong1',
                '<Event desc="giong2" type="lexical" extent="previous"/>',
                '-zia4',
            ],
            '<Sync time="409.946"/>',
        ]

    def test_標頭(self):
        self.原本 = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Trans SYSTEM "trans-14.dtd">
<Trans scribe="Administrator" audio_filename="AT-1" version="13" version_date="171224">
<Speakers>
<Speaker id="spk1" name="??" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk2" name="????" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk3" name="????" check="no" dialect="native" accent="" scope="local"/>
'''
        self.後來 = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<!DOCTYPE Trans SYSTEM "trans-14.dtd">',
            '<Trans scribe="Administrator" audio_filename="AT-1" version="13" version_date="171224">',
            '<Speakers>',
            '<Speaker id="spk1" name="??" check="no" dialect="native" accent="" scope="local"/>',
            '<Speaker id="spk2" name="????" check="no" dialect="native" accent="" scope="local"/>',
            '<Speaker id="spk3" name="????" check="no" dialect="native" accent="" scope="local"/>',
        ]

    def test_windows標頭(self):
        self.原本 = '''<?xml version="1.0" encoding="UTF-8"?>\r
<!DOCTYPE Trans SYSTEM "trans-14.dtd">\r
<Trans scribe="Administrator" audio_filename="AT-1" version="13" version_date="171224">\r
<Speakers>\r
<Speaker id="spk1" name="??" check="no" dialect="native" accent="" scope="local"/>\r
<Speaker id="spk2" name="????" check="no" dialect="native" accent="" scope="local"/>\r
<Speaker id="spk3" name="????" check="no" dialect="native" accent="" scope="local"/>\r
'''
        self.後來 = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<!DOCTYPE Trans SYSTEM "trans-14.dtd">',
            '<Trans scribe="Administrator" audio_filename="AT-1" version="13" version_date="171224">',
            '<Speakers>',
            '<Speaker id="spk1" name="??" check="no" dialect="native" accent="" scope="local"/>',
            '<Speaker id="spk2" name="????" check="no" dialect="native" accent="" scope="local"/>',
            '<Speaker id="spk3" name="????" check="no" dialect="native" accent="" scope="local"/>',
        ]
