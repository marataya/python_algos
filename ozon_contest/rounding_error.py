from io import StringIO
import sys

from dask.dataframe.core import idxmaxmin_agg

from ozon_contest.test_utils import prepare_input, compare_outputs
from time import time

if __name__ == '__main__':
    input_files, output_files = prepare_input('./input/rounding_error/*')
    begin = time()
    for idx_file in range(len(input_files)):
        print(input_files[idx_file])
        # putting program output into buffer to compare with answer later
        output_buffer = StringIO()
        tmp = sys.stdout
        sys.stdout = output_buffer
        # MAIN LOGIC
        with open(input_files[idx_file], "r") as input_file:
            t = int(input_file.readline())
            for _ in range(t):
                sum = 0
                n, p = map(int, input_file.readline().split())
                for _ in range(n):
                    price = int(input_file.readline())
                    sum += p * price / 100 % 1
                print(f'{round(sum, 2):.2f}')

        # MAIN LOGIC END
        sys.stdout = tmp

        compare_outputs(output_files[idx_file], output_buffer)
    end = time()
    print(f'{end-begin} sec')
