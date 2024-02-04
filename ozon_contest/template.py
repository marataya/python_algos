from io import StringIO
import sys
from ozon_contest.test_utils import prepare_input, compare_outputs
from time import time

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
            pass
        # MAIN LOGIC END
        sys.stdout = tmp

        compare_outputs(output_files[idx_file], output_buffer)
    end = time()
    print(f'{end-begin} sec')
