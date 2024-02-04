from io import StringIO
import sys
from ozon_contest.test_utils import prepare_input, compare_outputs
from time import time

if __name__ == '__main__':
    input_files, output_files = prepare_input('./input/battleships/*')

    begin = time()
    for idx_file in range(len(input_files)):
        # putting program output into buffer to compare with answer later
        output_buffer = StringIO()
        tmp = sys.stdout
        sys.stdout = output_buffer
        # MAIN LOGIC
        sets = []
        with open(input_files[idx_file], "r") as input_file:
            n = int(input_file.readline())
            for _ in range(n):
                row = [int(x) for x in input_file.readline().split()]
                sets.append(row)

        for idx, row in enumerate(sets):
            result = {}
            for ship in row:
                if ship not in result:
                    result[ship] = 1
                else:
                    result[ship] += 1
            if 4 in result and result[4] == 1 and 3 in result and result[3] == 2 and 2 in result and result[2] == 3 and 1 in result and result[1] == 4:
                print('YES', end=("\n" if idx != len(sets)-1 else ""))
            else:
                print('NO', end=("\n" if idx != len(sets)-1 else ""))
        # MAIN LOGIC END
        sys.stdout = tmp

        compare_outputs(output_files[idx_file], output_buffer)
    end = time()
    print(f'{end-begin} sec')
