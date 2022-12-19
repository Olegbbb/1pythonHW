x = int(input("Введите X: "))
y = int(input("Введите Y: "))
if x == 0 or y == 0:
    if x == y:
        print ("Точка в начале системы координат")
    elif x == 0:
        print("Точка лежит на оси X")
    elif y == 0:
        print ("Точка лежит на оси Y")
elif x > 0 and y > 0:
    print ("1 четверть")
elif x > 0 and y < 0:
    print("2 четверть")
elif x < 0 and y < 0:
    print ("3 четверть")
elif x < 0 and y > 0:
    print ("4 четверть")