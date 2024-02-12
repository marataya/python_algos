from io import StringIO
import sys
import json
from ozon_contest.test_utils import prepare_input, compare_outputs
from time import time


def count_infected_files(data, hacked_file_in_parent_dir=False):
    file_count = 0

    if 'files' in data:
        for file in data['files']:
            if hacked_file_in_parent_dir:
                file_count += len(data['files'])
                break
            if  file.endswith('.hack'):
                hacked_file_in_parent_dir = True
                file_count += len(data['files'])
                break

    if 'folders' in data:
        for folder in data['folders']:
            file_count += count_infected_files(folder, hacked_file_in_parent_dir)

    return file_count


if __name__ == '__main__':
    input_files, output_files = prepare_input('./input/count_infected_files/*')
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
                json_data = []
                data = ''
                for _ in range(n):
                    line = input_file.readline().strip().rstrip("\r\n").rstrip("\n")
                    data += line
                json_data = json.loads(data)
                infected_files = count_infected_files(json_data)
                print(infected_files)
        # MAIN LOGIC END
        sys.stdout = tmp

        compare_outputs(output_files[idx_file], output_buffer)
    end = time()
    print(f'{end - begin} sec')
