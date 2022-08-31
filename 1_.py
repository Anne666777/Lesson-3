def my_func():
    try:
        var_1 = float(input("Enter number a: "))
        var_2 = float(input("Enter number b: "))
        div = var_1 / var_2
    except ZeroDivisionError:
        return "Division by zero cannot be performed"
    else:
        return div


my_div = my_func()
print(my_div)
