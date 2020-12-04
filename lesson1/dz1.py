name = str
age = str
count = int
countAge = int
while True:

    if name != str and name != "":

        age = input("Введите ваше возраст: ")
        if age == "" and countAge == int:
            print("Возраст!")
            countAge = 0
            continue
        elif age == "" and countAge == 0:
            print("Возраст!")
            countAge = countAge + 1
            continue
        elif age == "" and countAge == 1:
            print(f"Пока {name}")
            break
        age = int(age)  # Here you need to make a hint of an error

        if 25 >= age >= 10:
            print("Привет %s ты молод тебе %d будешь лесарубом" % (name, age))
            break
        elif 45 >= age > 25:
            print("Привет %s ты не молод и не стар тебе %d будешь плотником" % (name, age))
            break
        elif 65 >= age > 45:
            print("Привет %s ты зрел тебе %d будешь плотником директором" % (name, age))
            break
        elif age > 65:
            print("Привет %s тебе %d ты старец Фура тебе в Форт бояр " % (name, age))
            break
        else:
            print("Привет %s тебе %d ты мал и глуп иди учись " % (name, age))
            break
    else:
        name = input("Введите ваше имя: ")
        if count == int and name == "":
            print("Имя!")
            count = 0
            continue
        elif count == 0 and name == "":
            print("Говорю жишь имя")
            count = count + 1
            continue
        elif count == 1 and name == "":
            print("Пока дружок")
            break
