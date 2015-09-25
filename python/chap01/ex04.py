# -*- coding: utf-8 -*-

""" 04. Ký tự thành phần
1) Tokenize câu sau: "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

2) Lấy ra ký tự đầu tiên của các từ ở vị trí 1, 5, 6, 7, 8, 9, 15, 16, 19; với các từ còn lại lấy ra ký tự thứ 2. Tạo ra một map từ các ký tự này tới vị trí của từ trong câu.
"""

def main():
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

    words = sentence.split()
    char_dict = {}

    keys = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    index_dict = {key: None for key in keys}

    for i in xrange(len(words)):
        w = words[i]
        if index_dict.has_key(i+1):
            char_dict[w[0]] = i+1
        else:
            char_dict[''.join(w[0:2])] = i+1

    print 'Input sentence: %s' % sentence
    print repr(words)
    print repr(char_dict)

if __name__ == '__main__':
    main()

    
            

            

