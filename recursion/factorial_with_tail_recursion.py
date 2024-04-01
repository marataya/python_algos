'''
Tail recursion is a specific type of recursion in programming where the recursive call is the last operation performed by a function before it returns. This characteristic allows for potential optimizations by compilers, as the function's call stack frame doesn't need to be preserved for further processing after the recursive call.

Here's a breakdown of tail recursion:

Key Points:

The recursive call is the last statement in the function body.
There are no further operations or calculations after the recursive call.
This allows the compiler to potentially replace the function call with a jump instruction, avoiding the overhead of creating a new stack frame for each recursive step.
Benefits:

Improved performance: In some cases, tail recursion can lead to significant performance gains, especially for deep recursions, as the stack space usage is minimized.
Potential for functional style: Tail recursion aligns well with functional programming principles, where functions are pure and often avoid side effects.
'''
import time

# compiler optimized tail recursive function
def factorial_tail_recursive(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial_tail_recursive(n - 1, n * acc)

if __name__ == '__main__':
    begin = time.time()
    print(factorial_tail_recursive(100))
    end = time.time()
    print(f'Time: {end - begin} ms')

