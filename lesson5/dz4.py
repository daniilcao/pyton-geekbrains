import re

lang = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыри",
}
with open("dz4.txt", "r") as f_obj:
    f = open("dz4end.txt", "w")
    print(*[f"{v} - {k}" for k, v in
            enumerate(
                [lang.get(v) for k, v in enumerate(re.sub(r"[—]", "", f_obj.read()).split()) if lang.get(v) != None],
                1)], file=f, sep='\n')
    f.close()
