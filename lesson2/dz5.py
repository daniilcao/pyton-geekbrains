my_list = [7, 5, 5, 3, 3, 2]

while True:
    num = input("Set number:")
    if num.lstrip('-').isdigit():
        int_n = int(num)
        if my_list.count(int_n):
            i = my_list.index(int_n)
            c = my_list.count(int_n)
            my_list.insert(i+c, int_n)
        else:
            s_num = 0
            for k, v in enumerate(my_list):
                if int_n > v:
                    if s_num < v:
                        s_num = v
            if s_num != 0:
                my_list.insert(0, int_n)
            else:
                my_list.append(int_n)
    print(my_list)
