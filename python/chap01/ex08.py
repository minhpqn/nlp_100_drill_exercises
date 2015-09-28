# -*- coding: utf-8 -*-
import string
import re

### 08. Xâu mật mã
# Từ các ký tự của một xâu cho trước, cài đặt hàm có tên cipher để mã hoá xâu như sau:
# - Nếu là ký tự tiếng Anh ở dạng thường (lower-case characters) thì chuyển thành ký tự có mã (219 - mã của ký tự hiện tại).
# - Các ký tự khác giữ nguyên.
# Sử dụng hàm đã viết để mã hoá và giải mã các xâu ký tự tiếng Anh.

def cipher(s):
    news = ''
    for i in xrange(len(s)):
        newc = s[i]
        if re.search(r'[a-z]', s[i]):
            newc = chr(219 - ord(s[i]))
        news += newc

    return news


def decipher(s):
    news = ''
    for i in xrange(len(s)):
        tempc = chr(219 - ord(s[i]))
        newc = s[i]
        if re.search(r'[a-z]', tempc):
            newc = tempc
        news += newc

    return news


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '

    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    s = 'aBcDef123'
    z = cipher(s)
    print 'Xâu mã hoá của %s là %s' % (s, z)

    orig = decipher(z)
    print 'Xâu giải mã của %s là %s' % (z, orig)

if __name__ == '__main__':
    main()
    
        



