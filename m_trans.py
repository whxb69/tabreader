# -*- coding:utf-8 -*-
import cgitb
import urllib.request
import execjs
import re
cgitb.enable()
from bookui import *

class Py4Js:
    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";                                                                                                                                                                         
        var b = 406644;
        var b1 = 3293161072;

        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";

        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };

    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)

class tfunction(Ui_MainWindow):
    def trans(self,temp):
        js = Py4Js()
        reobj0 = re.compile(r'^\n',
                            re.M)
        ResultList = reobj0.split(temp)
        temp = ''
        for i in range(len(ResultList)):
            temp += re.sub(r'\n', " ", ResultList[i])
            temp += '\r\n\r\n'
        origin = 0
        last = 0
        String = ''
        i = -1
        k = 0
        result = [""] * (round(len(temp) / 1200) + 1)
        while i < len(temp):
            i += 1
            if i != len(temp):
                if temp[i] == '.' or temp[i] == '?':
                    if i - last < 1200:
                        origin = i
                        continue
                    else:
                        i = origin
                        content = temp[last:origin]
                        last = origin
                else:
                    if i - last >= 1200:
                        i = origin
                        content = temp[last:origin]
                        last = origin
                    else:
                        continue
            else:
                content = temp[last:len(temp)]
            tk = js.getTk(content)
            content = urllib.parse.quote(content)
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            req = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(req)
            result[k] = response.read().decode('utf-8')
            k = k + 1
        BraceCount = 2
        Searched = 0
        BeginIndex = 0
        EndIndex = 0
        for i in range(0, round(len(temp) / 1200) + 1):
            for k in range(2, len(result[i])):
                if result[i][k] == '[':
                    BraceCount += 1
                    Searched = 1
                    BeginIndex = k
                if result[i][k] == ']':
                    BraceCount -= 1
                    Searched = 1
                    EndIndex = k
                if Searched == 1 and BraceCount == 2 and EndIndex - BeginIndex > 3:
                    Searched = 0
                    try:
                        temp = result[i][BeginIndex:k + 1].split('","')[0].split('["')[1]
                        # print(temp, end='\n\n')
                        # print(result[i][BeginIndex:k+1])
                    except:
                        break
                    String += temp
        String = String.replace("\\r\\n", "\n")
        return String

