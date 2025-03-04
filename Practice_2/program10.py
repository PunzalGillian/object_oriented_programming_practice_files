#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))

for i in range (num_1 + 1, num_2 ):
    print(i)