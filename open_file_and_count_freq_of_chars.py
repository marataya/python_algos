"""
Write a Python program that inputs a document and then outputs a barchart plot of the frequencies of each alphabet character that appears in that document
"""
import collections
import re

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        text = f.read()
        clean_text = re.sub('[^A-Za-z0-9]', '', text).upper()
        freqs = collections.Counter(clean_text)
        total_freq = freqs.total()
        max_freq = freqs.most_common(1)[0][1]
        sorted_items = freqs.most_common()
        sorted_items.sort(key=lambda x: x[0])
        print(sorted_items)
        for k,v in sorted_items:
            print(f'{k}: {"#" * v} {v*100/total_freq:.2f} %')

