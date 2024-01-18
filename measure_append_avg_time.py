from time import time


def compute_average(n: int) -> float:
    data = []
    start = time()
    for k in range(n):
        data.append(None)

    end = time()
    return (end - start) / n

if __name__ == '__main__':
    print(f'{compute_average(100)*1000000:0.6f} millisec')
    print(f'{compute_average(1000)*1000000:0.6f} millisec')
    print(f'{compute_average(10000)*1000000:0.6f} millisec')
    print(f'{compute_average(100000)*1000000:0.6f} millisec')
    print(f'{compute_average(1000000)*1000000:0.6f} millisec')
