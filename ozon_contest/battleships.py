if __name__ == '__main__':
    sets = []
    with open("input/battleships/7", "r") as input_file:
        n = int(input_file.readline())
        for _ in range(n):
            row = [int(x) for x in input_file.readline().split()]
            sets.append(row)

    for row in sets:
        result = {}
        for ship in row:
            if ship not in result:
                result[ship] = 1
            else:
                result[ship] += 1
        if 4 in result and result[4] == 1 and 3 in result and result[3] == 2 and 2 in result and result[2] == 3 and 1 in result and result[1] == 4:
            print('YES')
        else:
            print('NO')
