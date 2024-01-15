'''
Recursive Python function that rearranges a sequence of integer values so that all the even values appear before all the odd values
'''

def even_before_odd(list:list[int]) -> list[int]:
    n = len(list)
    if n <= 1:
        return list
    if list[0] % 2 == 0:
        return [list[0]] + even_before_odd(list[1:])
    else:
        return even_before_odd(list[1:]) + [list[0]]

if __name__ == '__main__':
    print(even_before_odd([1,2,3,4,5,6]))
