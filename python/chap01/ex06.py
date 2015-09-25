# -*- coding: utf-8 -*-
from ex05 import get_char_ngrams

# 1) Sinh ra tập X và Y tương ứng là tập các character bi-gram từ hai xâu ký tự "paraparaparadise" và "paragraph".
# 2) Sinh ra các tập hợp union, intersection và difference của X và Y
# 3) Kiểm tra xem bi-gram 'se' có thuộc tập X (Y) hay không?

def main():
    s1 = 'paraparaparadise'
    s2 = 'paragraph'

    X = set(get_char_ngrams(s1, 2))
    Y = set(get_char_ngrams(s2, 2))

    print s1
    print s2

    print 'X = %s' % X
    print 'Y = %s' % Y

    union = X.union(Y)
    intersection = X.intersection(Y)
    difference = X.difference(Y)

    print 'union: %s' % union
    print 'intersection: %s' % intersection
    print 'difference: %s' % difference

    bgr = 'se'
    if bgr in X:
        print '%s is in X' % bgr
    else:
        print '%s is not in X' % bgr

    if bgr in Y:
        print '%s is in Y' % bgr
    else:
        print '%s is not in Y' % bgr    

if __name__ == '__main__':
    main()
    


