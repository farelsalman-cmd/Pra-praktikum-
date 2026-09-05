#Operasi Aritmatika dan Komperasi
#panjang
p = 12
#lebar
l = 5
#tinggi
t = 8
#Cari Luas, Volume, Keliling
print("===============================")
#Luas
hasil = 2 * (p * l + p * t + l * t)
print("Luas balok =",hasil)
#Volume
hasil = p * l * t
print("Volume = ",hasil)
#Keliling
hasil = 4 * (p + l + t)
print("Keliling balok =", hasil)
print("===============================")

#Apakah luas bangunan > 50 ?
luas = 2 * (p * l + p * t + l * t)
pembanding = 50
hasil = luas > pembanding
print(luas,">",pembanding,"=",hasil)
#Apakah volume bangunan = 480 ?
l = p * l * t
p = 480
hasil = l == p
print(l,"==",p,"=",hasil)
print("===============================")