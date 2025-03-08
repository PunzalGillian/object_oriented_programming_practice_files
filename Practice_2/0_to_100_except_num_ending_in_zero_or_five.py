#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

count = 0 
num_list_without_zero_and_five = []

while count != 100:
    count += 1

    if count % 10 != 0 and count % 5 != 0:
        num_list_without_zero_and_five.append(count)

print(num_list_without_zero_and_five)
        