from stack import ArrayStack

def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


if __name__ == '__main__':
    file = open('input_for_reverse_file.txt', 'r')
    for line in file:
        print(line)
    reverse_file('input_for_reverse_file.txt')
    file = open('input_for_reverse_file.txt', 'r')
    for line in file:
        print(line)
