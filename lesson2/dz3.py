cont = ["Зима",
        "Зима",
        "Весна",
        "Весна",
        "Весна",
        "Лето",
        "Лето",
        "Лето",
        "Осень",
        "Осень",
        "Осень",
        "Зима"]

while True:
    num = int(input("set month:")) - 1
    if 0 > num or num > 11:
        print("err")
        continue
    print(cont[num])

# --------------------------------
m = {
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима",
}
while True:
    num = int(input("set month:"))
    if 1 > num or num > 12:
        print("err")
        continue
    print(m.get(num))
