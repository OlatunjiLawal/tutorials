import sys

def main():
    try: 
        position = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Please provide a valid integer as an argument.")
        sys.exit(1)
    
    pos_number = fib_sequence(position)
    print(f"The Fibonacci number at position {position} is {pos_number}.") 

def fibonacci(n):
    
    a = 0
    b = 1

    for _ in range(1, n):
        a, b = b, a + b
    return a

def fib_sequence(position):
    if position < 1:
        print("Please enter valid number (positive integer).")
    fib_number = fibonacci(position) 
    return fib_number

if __name__ == "__main__":
    main()

