def BtoG(a):
    i = 0
    while i < len(a):
        print(a[i], end="")
        if a[i] == "a":
            print("ga", end="")
        elif a[i] == "i":
            print("gi", end="")
        elif a[i] == "u":
            print("gu", end="")
        elif a[i] == "e":
            print("ge", end="")
        elif a[i] == "o":
            print("go", end="")
        i = i+1


def GtoB(a):
    i = 0
    while i < len(a):
        if a[i] == "a" or a[i] == "i" or a[i] == "u" or a[i] == "e" or a[i] == "o":
            if a[i:i+3] == "aga":
                print("a", end="")
                i += 1
            elif a[i:i+3] == "igi":
                print("i", end="")
                i += 1
            elif a[i:i+3] == "ugu":
                print("u", end="")
                i += 1
            elif a[i:i+3] == "ege":
                print("e", end="")
                i += 1
            elif a[i:i+3] == "ogo":
                print("o", end="")
                i += 1
        else:
            print(a[i], end="")
        i += 1


print("1. Bahasa to G \n2. G to Bahasa")
pilihan = int(input("Pilihan : "))
kalimat = input("Masukkan Kalimat : ")

if pilihan == 1:
    BtoG(kalimat)
elif pilihan == 2:
    GtoB(kalimat)
