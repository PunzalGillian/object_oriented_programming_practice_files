#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

even_num_list = []
for i in range(0,101):
    if i % 2 == 0:
        even_num_list.append(i)
print(even_num_list)
