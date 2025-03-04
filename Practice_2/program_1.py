#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

while True:
    try:
        num_1 = float(input("Enter a valid number: "))
        num_2 = float(input("Enter a valid number: "))

        if num_1 < num_2:
            print(f"{num_1} is the smaller number")
        elif num_1 > num_2:
            print(f"{num_2} is the smaller number")
        else:
            print("Both numbers are equal")
        break
    except ValueError:
        print("Enter a valid number")

