import random


def main():
    # c = [random.randint(1, 15) for _ in range(20)]
    c = [2, 6, 2, 9, 9, 13, 2, 8, 6, 4, 1, 6, 5, 10, 15, 2, 6, 1, 5, 4]
    print(c)
    result = []  # list of lists
    tmp = []
    last_direction = 0
    last_element = c[0]

    for i in range(len(c)):
        if c[i] == last_element:
            direction = 0
        else:
            direction = int((c[i] - last_element) / abs(
                c[i] - last_element))  # math trick - divide by the magnitude to get the direction (-1/1)
        last_element = c[i]
        if (last_direction & direction != 0) and len(tmp) > 1:
            result.append(tmp)
            tmp = []

        print(f'{last_direction:8d}, {direction:8d}, {c[i]:8d}')
        last_direction = last_direction if direction == 0 else direction

        tmp.append(c[i])
    if tmp:
        result.append(tmp)
    print(result)
    print()
    for s in result:
        if len(s) > 1 and s[0] > s[1]:
            s.reverse()
    print(result)


if __name__ == "__main__":
    main()
