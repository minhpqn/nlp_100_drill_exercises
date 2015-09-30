# -*- coding: utf-8 -*-
#!/usr/bin/python

import numpy as np

# 18. Sắp xếp các hàng theo thứ tự giảm dần của giá trị (numeric value) của cột thứ 3
# Viết chương trình thực hiện nhiệm vụ trên.
# Dùng lệnh sort để xác nhận (trong bài tập này, kết quả của chương trình của bạn với lệnh sort có thể khác nhau do có thể có các giá trị giống nhau trong cột thứ 3).

# Confirm with sort command
# % sort -r -n -k 3 ../../data/hightemp.txt

def sort_by_col3():
    f = open('../../data/hightemp.txt', 'rU')

    keys = []
    lines = []
    for line in f:
        line = line.rstrip()
        cols = line.split()
        val = float(cols[2])
        keys.append(val)
        lines.append(line)
        
    f.close()

    # get original indexes of sorted array using lambda
    # reference: http://stackoverflow.com/questions/6422700/how-to-get-indices-of-a-sorted-array-in-python
    # Python Lambda Function for anonymous function:
    # http://www.secnetix.de/olli/Python/lambda_functions.hawk
    # Python sorting:
    # https://wiki.python.org/moin/HowTo/Sorting#Key_Functions
    # try the solution with numpy.argsort
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html#numpy-argsort
    # indexes = np.array(keys).argsort()[::-1]
    
    indexes = sorted(range(len(keys)),key=lambda x:keys[x], reverse=True)
    for i in indexes:
        print lines[i]

def main():
    sort_by_col3()

if __name__ == '__main__':
    main()
    
    


