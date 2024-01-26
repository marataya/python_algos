'''
P-6.36 When a share of common stock of some company is sold, the capital gain (or, sometimes, loss) is the difference between the share’s selling price and the price originally paid to buy it. This rule is easy to understand for a single share, but if we sell multiple shares of stock bought over a long period of time, then we must identify the shares actually being sold. A standard accounting principle for identifying which shares of a stock were sold in such a case is to use a FIFO protocol—the shares sold are the ones that have been held the longest (indeed, this is the default method built into several personal finance software packages). For example, suppose we buy 100 shares at $20 each on day 1, 20 shares at $24 on day 2, 200 shares at $36 on day 3, and then sell 150 shares on day
4 at $30 each. Then applying the FIFO protocol means that of the 150 shares sold, 100 were bought on day 1, 20 were bought on day 2, and 30
were bought on day 3. The capital gain in this case would therefore be 100 · 10+20 · 6+30 ·(−6), or $940. Write a program that takes as input
a sequence of transactions of the form “buy x share(s) at y each” or “sell x share(s) at y each,” assuming that the transactions occur on consecutive days and the values x and y are integers. Given this
input sequence, the output should be the total capital gain (or loss) for the entire sequence, using the FIFO protocol to identify shares.
'''

import re
from dequeue import ArrayDequeue

if __name__ == '__main__':
    capital_gain = 0
    log = []

    with open('input_for_calculate_capital_gains.txt', 'r') as f:
        lines = f.readlines()
        # prompt: match number before word 'share'
        for line in lines:
            operation = line.split()[0]
            if operation not in ['buy', 'sell']:
                raise ValueError('Input string should contain BUY or SELL! Exiting with error')

            match = re.search(r'\d+\s*share', line)
            if match:
                volume = match.group().split()[0]
            else:
                raise ValueError('Input string should number of shares sold or purchased! Exiting with error')

            match = re.search(r'\d+\s+each', line)
            if match:
                price = match.group().split()[0]
            else:
                raise ValueError('Input string should contain price! Exiting with error')

            log.append([operation, int(volume), int(price)])

    print(log)

    trade_log = ArrayDequeue()
    total_volume = 0
    for x in log:
        if x[0] == 'buy':
            trade_log.add_last([x[1], x[2]])
        else:
            volume_sold = x[1]
            sell_price = x[2]
            while True:
                if trade_log.is_empty():
                    raise RuntimeError('Cannot sell stonks that are not bought before')
                curr = trade_log.first()
                volume_bought = curr[0]
                buy_price = curr[1]
                if volume_bought <= volume_sold:
                    capital_gain += (sell_price - buy_price) * volume_bought
                    volume_sold -= volume_bought
                    trade_log.delete_first()
                else:
                    capital_gain += (sell_price - buy_price) * volume_sold
                    curr[1] -= volume_sold
                    break
                # if total_volume
    print('Capital gain:',capital_gain)
