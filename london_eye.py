
def eye ():

    name = input("Enter you name: ")
    age = input("Enter your age: ")

    age = int(age)
    print(f"Hello {name} (age <{age}>)")

    LEage = 2022 - (1999 + age)

    print("You were " + str(LEage) + "years old when the london eye opened in 1999")
eye()