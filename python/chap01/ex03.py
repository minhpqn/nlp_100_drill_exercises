# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize
import string
import re

''' 03. Tokenize và thống kê số lượng ký tự của mỗi từ
1) Tokenize câu sau: "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
2) Đưa ra danh sách gồm số ký tự alphabet trong mỗi từ theo thứ tự xuất hiện của từ đó trong câu.
'''

# Return the number of alphabet characters in a string    
def char_count(w):
    num = 0
    for i in xrange(len(w)):
        if re.search(r'[a-zA-Z]', w[i]):
            num += 1
    return num        
    
# Given a list of words, return a list of number of alphabet characters
def get_num_chars(words):
    list1 = []

    for w in words:
        list1.append(char_count(w))

    return list1
    

if __name__ == '__main__':
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    
    print 'Input string %s' % sentence

    print '-- using simple tokenizer'
    words = sentence.split()
    print repr(words)
    print repr(get_num_chars(words))

    print '-- using nltk for tokenizing'
    words = word_tokenize(sentence)
    print repr(words)
    print repr(get_num_chars(words))
