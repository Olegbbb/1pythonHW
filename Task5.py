import math
xA = int(input("Введите координату x точки A: "))
yA = int(input("Введите координату y точки A: "))
xB = int(input("Введите координату x точки B: "))
yB = int(input("Введите координату y точки B: "))
print((f'Расстояние между точками равно {round(float(math.sqrt((xB - xA)**2 + (yB - yA)**2)),2)}'))