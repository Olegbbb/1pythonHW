quarter = int(input("Введите номер четверти: "))
if 0 < quarter < 5:
    if quarter == 1:
        print ("Возможные значения X(0; +∞), Y(0; +∞)")
    if quarter == 2:
        print ("Возможные значения X(0; +∞), Y(0; -∞)")
    if quarter == 3:
        print ("Возможные значения X(0; -∞), Y(0; -∞)")
    if quarter == 4:
        print ("Возможные значения X(0; -∞), Y(0; +∞)")
else:
    print("Нет такой четверти")