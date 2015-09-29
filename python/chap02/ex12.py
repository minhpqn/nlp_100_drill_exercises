# -*- coding: utf-8 -*-

# 12. Lưu dòng 1 vào file col1.txt, dòng 2 vào file col2.txt
# Trích xuất nội dung trong cột 1, cột 2 và lưu vào các file tương ứng: col1.txt và col2.txt.
# Thử thực hiện công việc chỉ dùng lệnh cut trong unix.

# Confirm by command cut
# % cut -f 1 ../../data/hightemp.txt > col1.txt
# % cut -f 2 ../../data/hightemp.txt > col2.txt

# Extract column n from given text file src and write to file dest
def extr_column(src, dest, n):
    fin = open(src, 'rU')
    fo = open(dest, 'w')

    for line in fin:
        line = line.rstrip()
        cols = line.split()
        col = cols[n-1]
        fo.write('%s\n' % col)
    
    fin.close()
    fo.close()

def main():
    filename = '../../data/hightemp.txt'
    extr_column(filename, 'col1.txt', 1)
    extr_column(filename, 'col2.txt', 2)

if __name__ == '__main__':
    main()
    
    
