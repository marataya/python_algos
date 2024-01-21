import glob
import re
import sys

def prepare_input(filename: str):
    files = glob.glob(filename)
    input_files = []
    output_files = []
    for file in files:
        if not re.search('\\.[a-zA-Z]+$', file):
            input_files.append(file)
        else:
            output_files.append(file)
    input_files.sort(key=lambda x: int(re.search("[^/]+$", x).group()))
    output_files.sort(key=lambda x: int(re.search("([^/]+)((?=\.[^.]+$))", x).group()))
    return input_files, output_files

def compare_outputs(filename, output_buffer):
    with open(filename, 'r') as output_file:
        reference_ouput = output_file.read()
        print(output_file.name)
        print(reference_ouput)
        print('>>>>>>>>>>OUTPUT<<<<<<<<')
        print(output_buffer.getvalue())
        if output_buffer.getvalue().rstrip() == reference_ouput:
            print('>>>>>>>>>>>>>> EQUAL\n\n')
        else:
            print('>>>>>>>>>>>> NOT EQUAL\n\n')
            sys.exit(1)
