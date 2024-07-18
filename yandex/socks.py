def is_even_socks(socks):
    total_socks = sum(socks)
    return total_socks % 2 == 0


if __name__ == '__main__':
    no_of_rooms = int(input())
    socks = map(int, input().split())
    sum = 0
    for x in socks:
        sum = sum + x
    print('YES' if sum % 2 == 0 else 'NO')

