import sys
def scitani (a, b):
    return a+b

def odcitani (a, b):
    return a-b

def nasobeni (a, b):
    return a*b

def deleni (a, b):
    return a/b
while True:   
    print("Vyber možnost: ")
    print("1.scitani")
    print("2.odcitani")
    print("3.nasobeni")
    print("4.deleni")
    print("5.ukoncit")
    moznost = input()
    if moznost=="5":
        sys.exit()
    a = float (input("Zadej prvni cislo:"))
    b = float (input("Zadej druhe cislo:"))
    vysledek = 0
    if moznost=="1":
        vysledek = scitani(a, b)
    if moznost=="2":
        vysledek = odcitani(a, b)
    if moznost=="3":
        vysledek = nasobeni(a, b)
    if moznost=="4":
        vysledek = deleni(a, b)

    print(f"vysledek je {vysledek}")

