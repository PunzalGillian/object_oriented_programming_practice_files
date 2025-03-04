#Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        num_difference = num_1 - num_2
        print(num_difference)
        break
    except ValueError:
        print("Enter a valid number")