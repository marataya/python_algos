from io import StringIO
import sys
from ozon_contest.test_utils import prepare_input, compare_outputs
from time import time
"""
В офисе стоит кондиционер, на котором можно установить температуру от 15 до 30 градусов.
В офис по очереди приходят n сотрудников. i-й из них желает температуру не больше или не меньше ai. После прихода каждого сотрудника определите, можно ли выставить температуру, которая удовлетворит всех в офисе.
"""

if __name__ == '__main__':
    input_files, output_files = prepare_input('./input/bitva_za_konder/*')
    begin = time()
    for idx_file in range(len(input_files)):
        # putting program output into buffer to compare with answer later
        output_buffer = StringIO()
        tmp = sys.stdout
        sys.stdout = output_buffer
        # MAIN LOGIC
        with open(input_files[idx_file], "r") as input_file:
            t = int(input_file.readline())
            for _ in range(t):
                n = int(input_file.readline())
                temp_range = list(range(15, 31))
                for _ in range(n):
                    line = input_file.readline()
                    sign = line[0:2]
                    temp = int(line[-3:])
                    if sign == ">=":
                        temp_range = list(filter(lambda x: x >= temp, temp_range))
                    else:
                        temp_range = list(filter(lambda x: x <= temp, temp_range))
                    if len(temp_range) == 0:
                        print(-1)
                    else:
                        print(temp_range[0])
                print()
        # MAIN LOGIC END
        sys.stdout = tmp

        compare_outputs(output_files[idx_file], output_buffer)
    end = time()
    print(f'{end-begin} sec')
