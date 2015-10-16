# -*- coding: utf-8 -*-
#!/usr/bin/python

# 70. Download và tiền xử lý dữ liệu
# Sử dụng dữ liệu liên quan đến sentiment polarity của các câu (download tại [đây](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz)), tạo dữ liệu chuẩn hoá (sentiment.txt) theo hướng dẫn dưới đây.
# 1. Thêm vào '+1' ở bắt đầu các dòng trong file rt-polarity.pos (giữa +1 và nội dung của câu cách nhau bởi ký tự trắng).
# 2. Thêm vào '-1' ở bắt đầu các dòng trong file rt-polarity.neg (giữa -1 và nội dung của câu cách nhau bởi ký tự trắng).
# 3. Kết hợp nội dung thu được trong phần 1 và 2 để tạo thành file sentiment.txt
# Sau khi đã thu được file sentiment.txt, xác nhận số lượng các câu với positive polarity và các câu với negative polarity.

"""
Download dữ liệu:
$ wget http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz
Decompress file:
$ tar -xvf rt-polaritydata.tar.gz
Xác nhận số lượng các câu với positive và negative polarities:
grep "^+1" ../../data/sentiment.txt | wc -l
grep "^-1" ../../data/sentiment.txt | wc -l
Tổng cộng có 5331 câu với '+1' polarity và 5331 câu với '-1' polarity
"""

# Add label lb to the beginning of lines in filename
# Return a list of lines
def add_labels(lb, filename):
    f = open(filename, 'rU')
    lines = f.readlines()
    lines = map( lambda x: ' '.join([lb, x]), lines )
    f.close()
    return lines

def main():
    fo = open('../../data/sentiment.txt', 'w')

    lines = add_labels('+1',  '../../data/rt-polaritydata/rt-polarity.pos')
    lines += add_labels('-1', '../../data/rt-polaritydata/rt-polarity.neg')

    fo.write( ''.join(lines) )

    fo.close()

if __name__ == '__main__':
    main()
    




