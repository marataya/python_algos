import sys


def main():
    n = int(input())
    keyboard = {k+1: v for k, v in enumerate(map(int, input().split()))}
    k = int(input())
    presses = (int(x) for x in input().split())

    for x in presses:
        keyboard[x] -= 1

    for k, v in keyboard.items():
        if v < 0:
            print("YES")
        else:
            print("NO")



if __name__ == '__main__':
    main()
