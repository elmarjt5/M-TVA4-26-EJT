# Ülessane 1

print("Tere, maailm!")

nimi = input("Mis on sinu nimi? ")
vanus = int(input("Kui vana sa oled? "))

print("Tere, maailm! Tervitan sind", nimi + "!")
print("Tere, maailm! Tervitan sind", nimi + "! Sa oled", vanus, "aastat vana.")

# Ülessanne 2 

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_kaib_koolis = True

print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_kaib_koolis))

# Teine võimalik väärtus on False
kas_kaib_koolis = False

print(kas_kaib_koolis)
print(type(kas_kaib_koolis))

# Ülessanne 3


import random

kommid = random.randint(10, 30)

print("Laual on", kommid, "kommi.")

ara_voetud = int(input("Mitu kommi soovid võtta? "))

if ara_voetud >= 0 and ara_voetud <= kommid:
    kommid = kommid - ara_voetud
    print("Lauale jäi", kommid, "kommi.")
else:
    print("Nii palju komme ei saa võtta.")



# Ülessanne 4

import math

umbermoot = float(input("Sisesta puu ümbermõõt sentimeetrites: "))

labimoot = umbermoot / math.pi

print("Puu läbimõõt on", round(labimoot, 2), "cm.")

#Ülessanne 5


n = float(input("Sisesta maatüki pikkus meetrites: "))
m = float(input("Sisesta maatüki laius meetrites: "))

diagonaal = (n ** 2 + m ** 2) ** 0.5

print("Maatüki diagonaal on", round(diagonaal, 2), "meetrit.")

#Ülessanne 6



aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))

kiirus = teepikkus / aeg

print("Sinu kiirus oli", round(kiirus, 2), "km/h")



#Ülessanne 7


a = float(input("Sisesta esimene arv: "))
b = float(input("Sisesta teine arv: "))
c = float(input("Sisesta kolmas arv: "))
d = float(input("Sisesta neljas arv: "))
e = float(input("Sisesta viies arv: "))

summa = a + b + c + d + e
keskmine = summa / 5

print("Arvude summa on", summa)
print("Aritmeetiline keskmine on", keskmine)

jagaja = int(input("Sisesta arv, millega summat jagada: "))

taisosa = summa // jagaja
jaak = summa % jagaja

print("Jagamise täisarvuline osa on", int(taisosa))
print("Jääk on", round(jaak, 2))


#Ülessanne 8



print("  @..@")
print(" (----)")
print(r"( \__/ )")
print('^^ "" ^^')


#Ülessanne 9


a = int(input("Sisesta kolmnurga esimene külg: "))
b = int(input("Sisesta kolmnurga teine külg: "))
c = int(input("Sisesta kolmnurga kolmas külg: "))

P = a + b + c

print("Kolmnurga ümbermõõt on", P)


#Ülessanne 10


pitsa_hind = 12.90

inimesed = int(input("Mitu inimest pitsat jagavad? "))

jootraha = pitsa_hind * 0.10
kokku = pitsa_hind + jootraha

iga_inimene = kokku / inimesed

print("Pitsa hind on", pitsa_hind, "eurot.")
print("Jootraha on", round(jootraha, 2), "eurot.")
print("Kokku tuleb maksta", round(kokku, 2), "eurot.")
print("Iga inimene maksab", round(iga_inimene, 2), "eurot.")


#Ülessanne 11


try:
    pitsa_hind = 12.90

    inimesed = int(input("Mitu inimest pitsat jagavad? "))

    if inimesed > 0:
        jootraha = pitsa_hind * 0.10
        kokku = pitsa_hind + jootraha
        iga_inimene = kokku / inimesed

        print("Pitsa hind on", pitsa_hind, "eurot.")
        print("Jootraha on", round(jootraha, 2), "eurot.")
        print("Kokku tuleb maksta", round(kokku, 2), "eurot.")
        print("Iga inimene maksab", round(iga_inimene, 2), "eurot.")
    else:
        print("Inimeste arv peab olema suurem kui 0.")

except ValueError:
    print("Viga! Palun sisesta täisarv.")

