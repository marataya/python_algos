import calendar
from datetime import date

key_array = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def print_month(month, year):
    idx = key_array.index(month)

    day = 1
    wd = date(year, idx+1, day).weekday()
    # print(wd)
    # wd = (wd + 1) % 7
    end = month_length[idx]
    if calendar.isleap(year) and idx == 1:
        end += 1

    print(f"{month} {year}".center(20))
    print("Su\tMo\tTu\tWe\tTh\tFr\tSa")
    print('\t'*wd, end='')
    while day <= end:
        print('{:2d}\t'.format(day), end='')
        wd = (wd + 1) % 7
        day += 1
        if wd == 0: print()
    print()



if __name__ == '__main__':
    print_month("January", 1988)
