def fizz_buzz ():
    
    for number in range(1, 20):
    
        if number % 3 == 0 and number % 4 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 4 == 0:
            print("buzz")
        else:
            print(number)
            
fizz_buzz()