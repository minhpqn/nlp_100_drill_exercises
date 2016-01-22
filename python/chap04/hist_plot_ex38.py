#!/usr/bin/python
# -*- coding: utf-8 -*-

# 38. Histogram
# Vẽ đồ thị histogram tần suất xuất hiện của các từ. Trục ngang là tần suất xuất hiện. Trục dọc là các từ.

import math
import matplotlib.pyplot as plt
import numpy as np
from word_freq_ex36 import get_word_frequency

if __name__ == '__main__':
    word_freq = get_word_frequency()
    freq_numbers = map( lambda x: word_freq[x], word_freq.keys() )

    # print len(freq_numbers)
    log_freq = map( lambda x: math.log(x), freq_numbers)

    plt.hist(log_freq, bins = 15, orientation='horizontal')
    plt.show()
    

