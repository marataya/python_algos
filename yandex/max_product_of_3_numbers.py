from math import prod
from itertools import permutations
ii_neg = []
ii_pos = []
ii_neg_neg = []

def add_elem_and_pop_min_or_max(min_or_max, val, ii_cur, lenn):
    ii_cur.append(val)
    if len(ii_cur) > lenn:
        ii_cur.pop(ii_cur.index(min_or_max(ii_cur, key=abs)))

def set_ii_for(val):
    global ii_neg, ii_pos, ii_neg_neg
    if val <= 0:
        add_elem_and_pop_min_or_max(min, val, ii_neg, 2)
        add_elem_and_pop_min_or_max(max, val, ii_neg_neg, 3)
    if val >= 0:
        add_elem_and_pop_min_or_max(min, val, ii_pos, 3)


### Тестирование:

def main():
    # Тестовые примеры
    test_cases = [
        [3, 5, 1, 7, 9, 0],
        [9, -3, 10, 55, 0, 45],
        [10, 9, 9],
        [-5, -3, -12],
        [1, 2, 3, 2, 1],
        [3, 5, 1, 7, 9, 0, 9, -3, 10, -999999],
        [0],
        # [3, 5, 1, 7, 9, 0, 9, -3, 10]*100000
    ]
    global ii_neg, ii_pos, ii_neg_neg
    for nums in test_cases:

        ii_neg = []
        ii_pos = []
        ii_neg_neg = []

        for val in nums:
            set_ii_for(val)

        def get_sort_values_of_indexes(*indexes):
            return sorted([val for val in indexes], key=abs)

        if not ii_pos:
            print(*get_sort_values_of_indexes(*ii_neg_neg))
        else:
            res = [ii_neg[len(ii_neg) + k - 3:] + ii_pos[-k:] for k in range(1, len(ii_pos) + 1, 2)]
            print(*get_sort_values_of_indexes(*max(res, key=lambda x: prod(get_sort_values_of_indexes(*x)))))

if __name__ == "__main__":
    main()
