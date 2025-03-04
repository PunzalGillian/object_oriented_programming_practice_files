#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

num_list = []
for i in range(0,10):
    num = float(input(f"Enter num_{i+1}: "))
    num_list.append(num)

result = num_list[0] - sum(num_list[1:])
print(f"Result: {result}")