def int_func(s):
    return s.capitalize()


s = input("set words with a blank").split()

str_concat = ""
for v in s:
    str_concat += int_func(v) if str_concat == "" else " " + int_func(v)

print(str_concat)
