#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_num_list = []
while True:
    try:
        for i in range (1,11):
            num = float(input(f"Enter num{i}: "))
            if num % 2 != 0:
                odd_num_list.append(num)

        print(f"The number of odd numbers is: {len(odd_num_list)}")
        break

    except ValueError:
        print("Error: Enter a valid number")