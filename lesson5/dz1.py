new_file = open("my_file.txt", 'w')
while True:
    data = input("Set new param:")
    if data == "":
        new_file.close()
        break
    new_file.write(f"{data}\n")

