#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

num_even = []
for i in range (0, 10):
    num = float(input(f"Enter num_{i+1}: "))
    
    if num % 2 == 0:
        num_even.append(num)

num_of_even_num = len(num_even)
print(f"The number of even numbers is : {num_of_even_num}")