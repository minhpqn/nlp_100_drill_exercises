# -*- coding: utf-8 -*-
#!/usr/bin/python

# 71. Stopwords
# Tạo ra danh sách các stopwords trong tiếng Anh. Sau đó viết 1 hàm để kiểm tra một từ có thuộc danh sách stopwords hay không. Hàm sẽ trả về giá trị TRUE nếu từ cho trước thuộc danh sách stopwords. Ngược lại hàm sẽ trả về giá trị FALSE. Sau đó viết mô tả về các test cho hàm đã viết.

# Danh sách các stopwords trong file: data/stopword.txt

def read_stopwords(filename):
    stopdict = {}
    f = open(filename, 'rU')
    for line in f:
        w = line.strip()
        if w == '': continue
        stopdict[w] = 1
    f.close()
    return stopdict

stopdict = read_stopwords('../../data/stopword.txt')    

def is_stopword(w):
    if stopdict.has_key(w):
        return True
    else:
        return False

def test(w, expected):
    got = is_stopword(w)
    if got == expected:
        print ' OK  %s\t%s' % (w, got)
    else:
        print '  X  %s\t%s' % (w, got)

def main():
    test('able', True)
    test('above', True)
    test('yourselves', True)
    test('man', False)
    test('home', False)
    test("you're", True)

if __name__ == '__main__':
    main()

