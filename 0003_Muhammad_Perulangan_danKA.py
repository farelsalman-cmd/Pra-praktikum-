
print('============================\n\tBilangan Ganjil\n============================')
angka = 1
while angka <=50:
    if(angka == 1):
        print('Bilangan ganjil',angka)
    angka = angka + 2
    print('Bilangan ganjil', angka)
    if(angka==49):
        break
print('============================')

print('============================\n\tBilangan Genap\n============================')
angka = 0
while angka<=50:
    if(angka ==0):
        print('Bilangan genap',angka)
    angka = angka + 2
    print('Bilangan genap',angka)
    if(angka==50):
        break
print('============================')

print('============================\n\tBilangan Prima\n============================')
angka = 1
while angka<=100:
    angka = angka + 1
    for i in range(2,angka):
        if angka%i==0:
            break
    else:
        print(angka,"Bilangan Prima ")
        if angka==97:
            break
print('============================')