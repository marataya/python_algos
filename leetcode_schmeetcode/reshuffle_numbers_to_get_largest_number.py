'''
This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510.
'''

def largest_number(nums: list):
    # convert numbers to strings
    nums = [str(x) for x in nums]

    # sort them in desc order
    nums.sort(reverse=True)

    return ''.join(nums)

if __name__ == '__main__':
    print(largest_number([10, 7, 76, 415]))
    print(largest_number([10, 88, 0, 1]))
