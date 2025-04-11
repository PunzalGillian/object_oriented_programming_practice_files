#Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

while True: 
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: ")) 
        total_sum = num_1 + num_2
        print(f"Total sum is: {total_sum:.2f}")
        break
    except ValueError:
        print("Error: Enter a valid number")