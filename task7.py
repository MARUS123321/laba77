def подсчет_букв():
    гласные = "аеёиоуыэюя"
    согласные = "бвгджзйклмнпрстфхцчшщ"
    строка = input("Введите строку: ")
    gl = 0
    sogl = 0
    for i in строка:
        if i.lower() in гласные:
            gl += 1
    for j in строка:
        if j.lower() in согласные:
            sogl += 1
    print("Количество гласных:", str(gl))
    print("Количество согласных:", str(sogl))

подсчет_букв()