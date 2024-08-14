import sys

position = int(sys.argv[1])

def fibonacci(n):
    
    a = 0
    b = 1

    for _ in range(1, n):
        a, b = b, a + b
    return a


if position < 1:
    print("Please enter valid number (positive integer).")
fib_number = fibonacci(position)

print(f"The Fibonacci number at position {position} is {fib_number}.")

