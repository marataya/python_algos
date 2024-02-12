"""
Условие задачи
Вы разрабатываете систему управления задачами. Система выполняет несколько действий:
M — запускает задачу.
R — перезапускает задачу.
C — отменяет задачу.
D — завершает задачу.

 В первую очередь, задача должна быть запущена. Запущенную задачу можно отменить, перезапустить или завершить
Перезапущенная задача отменяется системой. Отмененная задача запускается системой. Завершенная задача может быть
запущена заново. В итоге процесса обработки задачи она должна быть завершена, По данному процессу обработки одной задачи системой определите, был ли он проведен корректно, с учетом описанных выше правил.
"""

from io import StringIO
import sys
from ozon_contest.test_utils import prepare_input, compare_outputs
from time import time

def check_if_correct(sequence: str) -> bool:
    stack = []
    for c in sequence:
        if c == 'M':
            if stack and stack[-1] not in ('C', 'D'):
                return False
            stack.append(c)
        elif c == 'R':
            if not stack or stack[-1] != 'M':
                return False
            stack.append(c)
        elif c == 'C':
            if not stack or stack[-1] not in ('M', 'R'):
                return False
            # while stack is not None or stack[-1] != "M":
            #     stack.pop()
            stack.append(c)
        elif c == 'D':
            if not stack or stack[-1] not in ('M', 'R'):
                return False
            # while stack is not None and stack[-1] != "M":
            #     stack.pop()
            stack.append(c)
    return len(stack) == 0 or stack[-1] == 'D'

if __name__ == '__main__':
    input_files, output_files = prepare_input('./input/highload/*')
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
                sequence = input_file.readline()
                print("YES" if check_if_correct(sequence) else 'NO')

        # MAIN LOGIC END
        sys.stdout = tmp

        compare_outputs(output_files[idx_file], output_buffer)
    end = time()
    print(f'{end-begin} sec')
