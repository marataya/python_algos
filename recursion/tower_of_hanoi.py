# prompt: algorithn tower of hanoi recursive

def hanoi(n, source, destination, via):
    if n == 1:
        print(f"Move disk from {source} to {destination}")
    else:
        hanoi(n - 1, source, via, destination)
        hanoi(1, source, destination, via)
        hanoi(n - 1, via, destination, source)
