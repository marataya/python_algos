import random

def main():
    # c = [random.randint(1, 15) for _ in range(20)]
    c = [2, 6, 2, 9, 9, 13, 2, 8, 6, 4, 1, 6, 5, 10, 15, 2, 6, 1, 5, 4]
    print(c)
    result = []  # list of lists
    tmp = []
    last_direction = 0
    last_element = c[0]
    stack = []

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


    if len(result) == 1:
        print(1)
    else:
        while len(result) > 1:
            curr = result.pop(0)
            if len(curr) == 1:
                if (result[0][0] > result[0][1] and curr[0] > result[0][-1]) or (result[0][0] > result[0][1] and curr[0] > result[0][0]):
                    stack.push(curr[0])
            else:
                if (curr[0] < curr[1] and result[0][0] < result[0][1] and curr[0] > result[0][0]) or (curr[0] < curr[1] and result[0][0] > result[0][1] and curr[0] > result[0][-1]):
                    print(0)
                    break
                if (curr[0] > curr[1] and result[0][0] < result[0][1] and curr[-1] > result[0][0]) or (curr[0] > curr[1] and result[0][0] > result[0][1] and curr[-1] > result[0][-1]):
                    print(0)
                    break
        for i in range(len(stack)-1):
            if stack[i] > stack[i+1]:
                print(0)
                break
        else:
            print(1)

if __name__ == "__main__":
    main()
