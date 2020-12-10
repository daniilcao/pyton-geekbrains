product = []
product_flash = {}

while True:

    if product_flash.get("название") is None:
        name_product = input("name Product:")
        if len(name_product) == 0:
            print("non name Product")
            continue
        product_flash["название"] = name_product

    if product_flash.get("цена") is None:
        price_product = input("Price:")
        if len(price_product) <= 0 or price_product.isdigit() is False:
            print("non Price:")
            continue
        product_flash["цена"] = int(price_product)

    if product_flash.get("количество") is None:
        count_product = input("Product cont:")
        if len(count_product) <= 0 or count_product.isdigit() is False:
            print("non Product cont:")
            continue
        product_flash["количество"] = int(count_product)

    i = len(product) == 0 if 1 else len(product)
    product.append(tuple((int(i), product_flash.copy())))
    product_flash.clear()

    res_data = {
        "название": [],
        "цена": [],
        "количество": [],
        "ед": ["шт."]
    }

    for _, v in enumerate(product):
        name = v[1].get("название")
        r_name = res_data.get("название")
        r_name.append(name)

        name = v[1].get("цена")
        r_name = res_data.get("цена")
        r_name.append(name)

        name = v[1].get("количество")
        r_name = res_data.get("количество")
        r_name.append(name)

    print(res_data)
