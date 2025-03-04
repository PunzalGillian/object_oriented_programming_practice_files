#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

count = 0
odd_num_list = []

while count != 100:
    count += 1
    if count % 2 != 0:
        odd_num_list.append(count)

print(odd_num_list)
        
