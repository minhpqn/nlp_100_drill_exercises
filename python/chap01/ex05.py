# -*- coding: utf-8 -*-

# 05. n-gram
# 1) Viết hàm sinh ra tất cả các n-gram từ một dãy cho trước (dãy ký tự hoặc danh sách).
# 2) Sử dụng hàm đã viết, sinh ra word bi-gram và character bi-gram từ câu sau: "I am an NLPer"

def get_ngrams(arr, n, delim = ''):
    ngrams = []
    for i in xrange(len(arr)):
        _min = i
        _max = _min + n - 1
        if _max >= len(arr):
            break

        ngrams.append(delim.join(arr[_min:_max+1]))

    return ngrams

def get_char_ngrams(s, n):
    chars = []
    chars[:0] = s

    chars.insert(0, '_BOS_')
    chars.append('_EOS_')

    return get_ngrams(chars, 2)

def get_word_ngrams(s, n):
    words = s.split()
    words.insert(0, '_BOS_')
    words.append('_EOS_')

    return get_ngrams(words, 2, '/')

def main():
    s = 'I am an NLPer'

    word_bigrams = get_word_ngrams(s, 2)
    char_bigrams = get_char_ngrams(s, 2)

    print 'input string: %s' % s
    print 'word bi-grams'
    print word_bigrams
    print 'charactere bi-grams'
    print char_bigrams

if __name__ == '__main__':
    main()
    



    

