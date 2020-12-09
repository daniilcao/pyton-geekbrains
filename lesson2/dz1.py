mixType = [1, "Name", True, set("contetn"), {"name": "Anton"}, bytes(12), None, TypeError, (1, "12", False), 1.3,
           complex(5, 6), ["name", "Fname"]]
for k in mixType:
    res = type(k)
    print(res)
