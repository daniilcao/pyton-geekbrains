num = 3
i = 0
concat = 0
while i < 3:
    if i == 0:
        concat = num
    if i == 1:
        concat = concat + int(str(num) + str(num))
    if i == 2:
        concat = concat + int(str(num) + str(num) + str(num))
    i = i + 1
print(f"Res data -> {concat}")

