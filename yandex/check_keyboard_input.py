def find_if_correct(a, b):
    # a = input().replace('\r', '')
    # b = input().replace('\r', '')

    result = ''
    cursor = 0
    curr_command = ''
    command_mode = False

    for char in b:
        if command_mode:
            if char == '>':
                command_mode = False
                curr_command += char

                if curr_command == "<delete>":
                    if cursor < len(result):
                        result = result[:cursor] + result[cursor + 1:]
                        # cursor -= 1
                elif curr_command == "<bspace>":
                    if cursor > 0:
                        result = result[:cursor-1] + result[cursor:]
                        cursor -= 1
                elif curr_command == "<left>":
                    if cursor > 0:
                        cursor -= 1
                elif curr_command == "<right>":
                    if cursor < len(result):
                        cursor += 1

                curr_command = ''
            else:
                curr_command += char
        else:
            if char.isalpha():
                result = result[:cursor] + char + result[cursor:]
                cursor += 1
            else: # < is encountered
                command_mode = True
                curr_command += char

    print(result)
    if result == a:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    str = 'helto<left><bspace>l<delete>ochilds<bspace>'
    find_if_correct('hellochild', str)
    str = 'programming<left><left><right><delete>'
    find_if_correct('programming', str)
