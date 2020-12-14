res_data = 0
while True:
    in_data = input("put numbers separated by spaces or q for exit").split()
    q = in_data[(len(in_data) - 1)]
    (in_data.pop() if q == "q" else in_data)
    for v, k in enumerate(in_data):
        res_data += int(k)
    print(f"Res data{res_data}")
    if q == "q":
        break

