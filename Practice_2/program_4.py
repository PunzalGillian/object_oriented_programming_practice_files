#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        if num_2 == 0:
            print("Undefined number")
        else: 
            num_quotient = num_1 // num_2
            print(f"{num_quotient:.0f}")
        break
    except ValueError:
        print("Enter a valid number")