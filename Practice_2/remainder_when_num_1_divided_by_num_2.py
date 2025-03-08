#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        if num_1 == 0:
            print("Undefined")
        else:
            num_quotient = num_2 // num_1
            print(num_quotient) 
        break
    except ValueError:
        print("Enter a valid number")
