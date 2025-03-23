try:
    number = int(input("""Выберите число от "1" до "5" """))
    if number == 1:
        print("Соответствующее число - one")
    elif number == 2:
        print("Соответствующее число - two")
    elif number == 3:
        print("Соответствующее число - three")
    elif number == 4:
        print("Соответствующее число - four")
    elif number == 5:
        print("Соответствующее число - five")
    else:
        print("Введите пожалуйста коректное число.")

except ValueError:
    print("Ошибка: введено не число!")
