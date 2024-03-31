# Python code​​​​​​‌​‌​‌‌‌​‌‌​‌‌‌​‌​​‌‌‌​​‌‌ below
# You will need this class for your solution. Do not edit it.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
        # return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Complete the function definition for reverse_string.
# Use print("messages...") to debug your solution.

def reverse_string(my_string):
    # Use the "accumulator pattern."
    # Start with an "empty bucket" of the right data type,
    # and build the solution by filling the bucket within a loop.
    reversed_string = ""

    # Create a new stack
    stack = Stack()

    # Iterate through my_string and push the characters onto the stack
    for x in my_string:
        stack.push(x)

    print(stack)
    # Use a while loop with the exit condition that the stack is empty.
    # Within this loop, update reversed_string with characters popped off the stack.
    print(stack.is_empty())
    while not stack.is_empty():
        reversed_string += stack.pop()

    # Return the result
    return reversed_string

if __name__ == '__main__':
    test_string = "gninraeL nIdekniL htiw tol a nraeL"
    result = reverse_string(test_string)
    print(result)
