
num = float(input("Введите число от 0 до 10: "))
if num < 0 or num > 10:
    print("Число не в диапазоне от 0 до 10")
    exit()
elif num <=3:
    print("Число в диапазоне от 0 до 3")
elif num <= 6:
    print("Число в диапазоне от 3 до 6")
else:
    print("Число  в диапазоне от 6 до 10")
    