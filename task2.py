YEAR = int(input("Enter year:  "))
if YEAR % 4 != 0:
    print("simple")
elif YEAR % 100 == 0:
    if YEAR % 400 != 0:
        print("visokostny")
    else:
        print("simple")
else:
    print("simple")

