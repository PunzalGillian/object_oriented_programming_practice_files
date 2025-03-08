#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        if num_1 != num_2:
            print("Not Equal")
        else:
            print("Equal")
        break
    except ValueError:
        print("Enter a valid number")
