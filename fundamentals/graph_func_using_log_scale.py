# prompt: plot graphs of functions  8n, 4n*log(n), 2n^2, n^3, and 2^n  using a logarithmic scale
import math

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.logspace(-1,3, 1000)
    # x = range(1, 1000)
    y1 = [8 * i for i in x]
    y2 = [4 * i * math.log2(i) for i in x]
    y3 = [2 * i * i for i in x]
    y4 = [i * i * i for i in x]
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(x, y1, y2, y3, y4)
    plt.show()
