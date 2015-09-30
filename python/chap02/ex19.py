# -*- coding: utf-8 -*-
#!/usr/bin/python

### 19. Sắp xếp theo tần suất xuất hiện
# Đưa ra tần suất xuất hiện của các giá trị trong cột 1; sắp xếp các giá trị trong cột 1 theo thứ tự từ cao đến thấp của tần suất xuất hiện.
# Chỉ dùng lệnh cut, uniq, sort để thực hiện nhiệm vụ.

# Confirm the output using unix commands:
# % cut -f 1 ../../data/hightemp.txt | sort | uniq -c | sort -rn

def sort_by_colfreq(filename, n):
    f = open(filename, 'rU')

    colfreq = {}
    for line in f:
        line = line.rstrip()
        cols = line.split()
        val = cols[n-1]
        if colfreq.has_key(val):
            colfreq[val] += 1
        else:
            colfreq[val] = 1
    f.close()

    keys = sorted(colfreq.keys(), key=lambda x:colfreq[x], reverse=True)
    for v in keys:
        print '%s %s' % (colfreq[v], v)

def main():
    sort_by_colfreq('../../data/hightemp.txt', 1)

if __name__ == '__main__':
    main()
    
    


