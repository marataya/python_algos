"""
    Implementation of a moving statistics by extending CircularBuffer.
    This computes Standard deviation in the same way that MovingAverage
    is computed.
"""
from circular_buffer import CircularBuffer

class Statistics(CircularBuffer):

    def __init__(self, size):
        """Store buffer in given storage."""
        CircularBuffer.__init__(self, size)
        self.total = 0
        self.sumSq = 0

    def getAverage(self):
        """Returns moving average (zero if no elements)."""
        if self.count == 0:
            return 0
        return self.total/self.count

    def getStdev(self):
        """Returns moving stdev (zero if fewer than one element)."""
        if self.count <= 1:
            return 0
        var = (self.sumSq - self.total*self.total/self.count)/self.count
        return var ** 0.5

    def remove(self):
        """Removes oldest value from non-empty buffer."""
        removed = CircularBuffer.remove(self)
        self.total -= removed
        self.sumSq -= removed*removed
        return removed

    def add(self, value):
        """Adds value to buffer, overwrite as needed."""
        if self.isFull():
            delta = self.buffer[self.low]
        else:
            delta = 0

        self.total += value - delta
        self.sumSq += value*value - delta*delta
        CircularBuffer.add(self,value)

    def __repr__(self):
        """String representation of moving average."""
        if self.isEmpty():
            return 'ma:[]'
        return 'ma:[{0:s}]:{1:f} {2:f}'.format(','.join(map(str,self)),
                                               self.getAverage(),
                                               self.getStdev())
if __name__ == '__main__':
    b = Statistics(5)
    for _ in range(10):
        b.add(_*_)
        print (b)
