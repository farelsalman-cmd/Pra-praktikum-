#0003_Muhammad_Literal_Data
#Nama Variabel
Nama = "Muhammad Farel Salman"
print("Nama  : ", Nama)
Umur = 18
print("Umur  : ", Umur)
Berat = 64.5 
print("Berat : ", Berat,"Kg")
print("\n")

#Ubah tipe data 
angka_string = "123"
angka_float = 45.67
angka_integer = 89

angka_int1 = int(angka_string)
angka_int2 = int(angka_float)
angka_float = float(angka_integer)
angka_str = str(angka_integer)

print("Angka = ", angka_int1,",type =", type(angka_int1))
print("Angka = ", angka_int2,",type =", type(angka_int2))
print("Angka = ", angka_float,",type =", type(angka_float))
print("Angka = ", angka_str,",type =", type(angka_str))
print("\n")

#Program input
nama = input("Masukan nama   : ")
usia = int(input("Masukan usia   : "))
tinggi = float(input("Masukan tinggi : "))
print("data : ",nama,",type =", type(nama))
print("data",usia,",type =", type(usia))
print("data",tinggi,",type =", type(tinggi))