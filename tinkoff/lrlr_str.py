"""
3 задание
Ограничение времени
3 секунды
Ограничение памяти
1024 МБ
Вам дана последовательность A, изначально состоящая из одного элемента 0 (A=(0)) и строка S длины N, состоящая только из символов «L» и «R».
Затем вы проделаете следующую операцию для 1, 2, 3: i=1,2,3,...,N:
Если Si=L, то вы вставите число i слева от числа i−1 в последовательность A. Если Si=R, то вы вставите число i справа от числа i−1 в последовательность A. Найдите последовательность, которая получится после всех операций.

Формат входных данных
В первой строке вводится одно целое число N(1⩽N⩽5⋅10^5) − длина строки S.
Во второй строке вводится строка S(∣S∣=N). Гарантируется, что S состоит только из символов «l» и «r».

Формат выходных данных

Выведите N+1 число через пробел − последовательность A, которая получится в результате применения N операций.

Замечание

Примеры данных
Пример 1
5
LRRRL
5
LRRRL
1 2 3 5 4 0
1 2 3 5 4 0
Пример 2
6
RRLLRR
6
RRLLRR
0 1 4 5 6 3 2
0 1 4 5 6 3 2

"""

if __name__ == '__main__':
    n = int(input())
    s = input()

    result = [0]
    last_pos = 0

    for i in range(n):
        if s[i] == 'L':
            pass
        else:
            last_pos += 1
        result.insert(last_pos, i + 1)

    print(" ".join(map(str, result)))

