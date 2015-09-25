# -*- coding: utf-8 -*-

""" 01. Trích xuất ký tự từ xâu ký tự
Từ xâu ký tự "MPyaktQrBoilk RCSahr", hãy trích xuất các ký tự ở vị trí 2,4,6,8,10,12,14,16,18,20 và kết hợp theo thứ tự đó để tạo thành 1 xâu ký tự mới (ký tự space cũng được tính, các ký tự được đánh số từ 1).
"""

def main():
    a_string = 'MPyaktQrBoilk RCSahr'
    
    # using extended slice syntax. I found this very python
    # http://docs.python.org/2/whatsnew/2.3.html#extended-slices
    new_string = a_string[1:21:2]

    print new_string

if __name__ == '__main__':
    main();


