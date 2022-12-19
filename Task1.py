day = int(input("Введите номер дня недели: "))
if 0 < day < 8:
    if day == 6 or day == 7:
        print("Да")
    else: 
        print("Нет")
else:
    print("Такого дня недели не существует")   