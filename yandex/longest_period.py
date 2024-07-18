def find_max_free_period(schedule):
    start = 0
    end = 0
    max_start = 0
    max_length = 0

    while end < len(schedule):
        if not schedule[end]:
            end += 1
            if end - start > max_length:
                max_start = start
                max_length = end - start
        else:
            start = end = end + 1

    if max_length == 0:
        return "0 0"
    else:
        return f"{max_start + 1} {max_start + max_length}"

# Считываем расписание из входных данных
schedule = []
for _ in range(4):
    line = input().strip()
    if line:
        busy_days = line.split()
        for day in busy_days:
            schedule.append(True)
    else:
        schedule.extend([False] * 7)

# Находим максимальный отрезок свободных дней
result = find_max_free_period(schedule)
print(result)