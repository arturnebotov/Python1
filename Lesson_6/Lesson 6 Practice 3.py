a = input("Please enter international underwear size ")
c = a.upper()

b = {
     'XXS':"Russia - 42 , Germany - 36 , USA - 8 , France - 38 , Great Britain - 24",
     'XS':"Russia - 44 , Germany - 38 , USA - 10 , France - 40 , Great Britain - 26",
     'S':"Russia - 46 , Germany - 40 , USA - 12 , France - 42 , Great Britain - 28",
     'M':"Russia - 48 , Germany - 42 , USA - 14 , France - 44 , Great Britain - 30",
     'L':"Russia - 50 , Germany - 44 , USA - 16 , France - 46 , Great Britain - 32",
     'XL':"Russia - 52 , Germany - 46 , USA - 18 , France - 48 , Great Britain - 34",
     'XXL':"Russia - 54 , Germany - 48 , USA - 20 , France - 50 , Great Britain - 36",
     'XXXL':"Russia - 56 , Germany - 50 , USA - 22 , France - 52 , Great Britain - 38",
}


def func():
    if c == 'XXS':
        print(b['XXS'])
    elif c == "XS":
        print(b['XS'])
    elif c == "S":
        print(b['S'])
    elif c == "M":
        print(b['M'])
    elif c == "L":
        print(b['L'])
    elif c == "XL":
        print(b['XL'])
    elif c == "XXL":
        print(b['XXL'])
    elif c == "XXXL":
        print(b['XXXL'])

print(func())