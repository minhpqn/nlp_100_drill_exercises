#!/usr/bin/python
# -*- coding: utf-8 -*-

# 39. Luật Zipf
# Vẽ đồ thị với trục ngang là rank của các từ theo tần suất xuất hiện (cao đến thấp), trục dọc là tần suất xuất hiện của các từ.

import math
import matplotlib.pyplot as plt
import numpy as np
from word_freq_ex36 import get_word_frequency

if __name__ == '__main__':
    word_freq = get_word_frequency()
    sorted_words = sorted(word_freq.keys(), key = lambda x: word_freq[x], reverse = True)
    word_ranks = range(1, len(sorted_words) + 1)
    sorted_freqs = map( lambda x: word_freq[x], sorted_words)

    # Draw scatter plot
    x = word_ranks
    y = sorted_freqs

    plt.scatter(x, y)
    plt.show()
    

    
    
