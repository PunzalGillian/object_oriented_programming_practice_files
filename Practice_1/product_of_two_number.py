#Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.

while True: 
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        product_num = num_1 * num_2
        print(f"Product of two numbers is {product_num:.0f}") 
        break
    except ValueError:
        print("Error: Enter a valid number.")
