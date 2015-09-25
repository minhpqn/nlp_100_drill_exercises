# -*- coding: utf-8 -*-

"""
00. Đảo ngược xâu ký tự
Hãy đảo ngược xâu ký tự "stressed" (theo thứ tự từ cuối xâu đến đầu xâu ký tự).
"""

def reverse_string(s):
    txt=''
    for i in xrange(len(s)-1, -1, -1):
        txt += s[i]

    return txt

# using extended slice syntax:
# http://docs.python.org/2/whatsnew/2.3.html#extended-slices
def pythonic_reverse_string(s):
    return s[::-1]

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '

    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))    

def main():
    s = 'stressed'
    print reverse_string(s)

    test(reverse_string('stressed'), 'desserts')
    test(reverse_string('abcdef'), 'fedcba')
    test(pythonic_reverse_string('stressed'), 'desserts')
    test(pythonic_reverse_string('abcdef'), 'fedcba')


if __name__ == '__main__':
    main()

    


