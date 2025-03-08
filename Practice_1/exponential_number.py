#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
while True: 
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        total = num_1 ** num_2
        print(f"The first number raised to the second number is {total:.0f}")
        break
    except ValueError:
        print("Error: Enter a valid number")

