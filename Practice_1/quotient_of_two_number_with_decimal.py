#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        quotient_num = num_1 / num_2
        print(f"Quotient of the two number is {quotient_num:.2f}")
        break
    except ValueError:
        print("Error: Enter valid number")
