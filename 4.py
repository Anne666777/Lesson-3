def power(a, b):
    res = 1
    for i in range(abs(b)): # Функция abs() — это встроенная функция,
        # возвращающая абсолютное значение числа. Она принимает целые,
        # с плавающей точкой и комплексные числа на вход.
        res *= a
    if b >= 0:
        return res
    else:
        return 1 / res


print(power(float(input("First number: ")), int(input("Second number: "))))
