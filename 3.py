def my_func(num1, num2, num3):
    if num1 >= num3 and num2 >= num3:
        return num1 + num2
    elif num2 < num1 < num3:
        return num1 + num3
    else:
        return num2 + num3


print(f'Amount: {my_func(int(input("Enter num_1: ")), int(input("Enter num_2: ")), int(input("Enter num_3: ")))}')
