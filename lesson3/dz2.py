def printUser(name, surname, year_birth, city, email, tell):
    print(f"name:{name}, surname:{surname}, year_birth:{year_birth}, city:{city}, email:{email}, tell:{tell}")


def validData(data):
    print(len(data))
    if len(data) <= 5 or len(data) > 6:
        return False
    else:
        return True


data_in = input("Set your name,surname,year_birth,city,email,tell with a space:").split()

if validData(data_in):
    printUser(*data_in)
else:
    print("invalid parameter")
