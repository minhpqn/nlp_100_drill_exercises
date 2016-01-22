#!/usr/bin/python
# -*- coding: utf-8 -*-

# 37. Top 10 từ xuất hiện nhiều nhất
# Vẽ đồ thị (ví dụ bar graph) của tần suất xuất hiện của 10 từ xuất hiện nhiều nhất trong văn bản.

import matplotlib.pyplot as plt
import numpy as np
from word_freq_ex36 import get_word_frequency

if __name__ == '__main__':
    word_freq = get_word_frequency()
    sorted_words = sorted(word_freq.keys(), key = lambda x: word_freq[x], reverse = True)
    top10_words = sorted_words[0:10]
    top10_freqs = map( lambda x: word_freq[x], top10_words );

    top10_words_u = map( lambda x: unicode(x, 'utf-8'), top10_words)
    # draw bar graph for top-10 words

    n_groups = len(top10_words)

    index = np.arange(n_groups)
    bar_width = 0.6
    opacity   = 0.5

    plt.bar(index, top10_freqs, bar_width,
            alpha=opacity,
            color='b')

    plt.xlabel('Words')
    plt.ylabel('Word frequencies')
    plt.title('Top 10 highest-frequency words')
    plt.xticks(index + bar_width, top10_words_u)

    # plt.tight_layout()
    plt.show()

    

    

        
