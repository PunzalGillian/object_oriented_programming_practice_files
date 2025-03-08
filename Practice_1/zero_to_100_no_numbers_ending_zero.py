#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

no_zero_num = []
for i in range (0,101):
    if i % 10 != 0:
        no_zero_num.append(i)
print(no_zero_num)