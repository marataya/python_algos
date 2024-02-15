"""
5 задание
Ограничение времени
8 секунд
Ограничение памяти
1024 МБ
Ваш друг Илья загадал массив A, состоящий из N элементов. Вы хотите найти сумму всех элементов массива, то есть  Илья обещал рассказать вам Q фактов про массив. i-й факт про массив это сумма чисел на отрезке
Определите, сможете ли вы найти сумму всех элементов массива A, после того, как Илья расскажет вам все Q фактов про массив. И в случае, если можно, выведите наименьшее количество фактов, с помощью которых можно восстановить массив.

Формат входных данных

В первой строке вводятся два целых числа N,Q − длина массива и число фактов, которые обещал рассказать Илья.
В следующих Q строках вводятся по 2 числа − описания фактов.

Формат выходных данных

Выведите ответ на задачу
−
−  «Yes» и в следующей строке наименьшее количество фактов, если вы сможете найти сумму всех элементов массива A, и «No» иначе.

Примеры данных
Пример 1
3 3
1 2
2 3
2 2
3 3
1 2
2 3
2 2
Yes
3
Yes
3
Пример 2
4 3
1 3
1 2
2 3
4 3
1 3
1 2
2 3
No
No
Пример 3
4 4
1 1
2 2
3 3
1 4
4 4
1 1
2 2
3 3
1 4

"""

def minimum_cover_interval(segments, target):
    if not segments:
        return 0
    min_start = min(seg[0] for seg in segments)
    max_end = max(seg[0] for seg in segments)
    if min_start > 1:
        return -1
    count = [0] * (max_end - min_start + 1)
    for seg in segments:
        count[seg[0] - min_start] = max(count[seg[0] - min_start], seg[1] - seg[0])
    reach = 0
    max_reach = 0
    target_start = 1 - min_start
    target_end = len(target) - min_start
    i = 0
    for i in range(target_start + 1):
        if i + count[i] < target_start:
            continue
        reach = max(reach, i + count[i])
    res = 1
    for i in range(i, len(count)):
        if reach >= target_end:
            break
        max_reach = max(max_reach, i + count[i])
        if reach <= i:
            reach = max_reach
            res += 1
    return res if reach >= target_end else -1



if __name__ == '__main__':
    n, q = map(int, input().split())
    segments = [list(map(int, input().split())) for _ in range(q)]
    result = minimum_cover_interval(segments, [x + 1 for x in range(n)])
    if result == -1:
        print("NO")
    else:
        print("YES")
        print(result)
