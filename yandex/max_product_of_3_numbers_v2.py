from itertools import permutations

def main():
    nums = (int(i) for i in "3 5 1 7 9 0 9 -3 10".split())

    max_value = float("-inf")

    try:
        arr = []              # если массив длиной 3-4
        for _ in range(5):
            arr.append(next(nums))
    except:
        for trio in permutations(arr, 3):
            multiply = trio[0]*trio[1]*trio[2]
            if multiply > max_value:
                max_value = multiply
                three_values = trio
        print(*three_values)
        exit()


    arr.sort()              # если массив длиной 5 и более

    min_values = [*arr[:2]] # тут будет 2 минимальных значения
    max_values = [*arr[2:]] # тут будут 3 максимальных значения

    for elem in nums:
        if elem < max(min_values):  # обновляем значения
            min_values.append(elem) # в списках, если
            min_values.sort()       # число соответствует
            del min_values[-1]      # условиям
            continue

        if elem > min(max_values):
            max_values.append(elem)
            max_values.sort()
            del max_values[0]

    arr = max_values + min_values    # перебираю все пары
    for trio in permutations(arr, 3):
        multiply = trio[0]*trio[1]*trio[2]
        if multiply > max_value:
            max_value = multiply
            three_values = trio
    print(*three_values)

if __name__ == "__main__":
    main()
