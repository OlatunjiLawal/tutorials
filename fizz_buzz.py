import sys

loopno = int(sys.argv[0])
fizzdiv = int(sys.argv[1])
buzzdiv = int(sys.argv[2])

def fizz_buzz ():
    
    for number in range(1, loopno):
    
        if number % fizzdiv == 0 and number % buzzdiv == 0:
            print("fizzbuzz")
        elif number % fizzdiv == 0:
            print("fizz")
        elif number % buzzdiv == 0:
            print("buzz")
        else:
            print(number)
            
fizz_buzz()