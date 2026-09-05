#Arirmatika Sederhana + - * /

#Operasi Tambah
hasil = 10 + 4
print(hasil)
print("\n")
#Operasi Pengurangan
hasil = 10 - 4
print(hasil)
print("\n")
#Operasi Perkalian
hasil = 10 * 4
print(hasil)
print("\n")
#Operasi Pembagian
hasil = 10 / 4
print(hasil)
print("\n")
#Operasi Eksponen
hasil = 10 ** 4
print(hasil)
print("\n")
#Operasi Modulus
hasil = 10 % 4
print(hasil)
print("\n")
#Operasi Floor Division
hasil = 10 // 4
print(hasil)
print("\n")

#Konversi Celcius ke satuan lain
# latihan konversi satuan temperature
# program konversi celcius ke satuan lain  print(“\nPROGRAM KONVERSI TEMPERATUR\n”)  
celcius = float(input("Masukan suhu dalam celcius : "))
print("Suhu adalah",celcius,"Celcius")
# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah",reamur, "Reamur")  
# fahrenheit 
fahrenheit = ((9/5) * celcius) + 32 
print("Suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")  
#kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah",kelvin, "Kelvin")
print("\n")

#Operasi Komperasi
# setiap hasil dari operasi komperasi adalah boolean   
# >,<,>=,<=,==,!=,is,is not  
a = 4
b = 2
# lebih besar dari > 
print("=============== Lebih besar dari (>)") 
hasil = a > 3 
print(a,">",b,"=",hasil) 
hasil = b > 3 
print(b,">",3,"=",hasil) 
hasil = b > 2 
print(b,">",2,"=",hasil)
#kurang dari < 
print("=============== Kurang dari (<)") 
hasil = a < 3 
print(a,"<",b,"=",hasil)
hasil = b < 3 
print(b,"<",3,"=",hasil)
hasil = b < 2 
print(b,"<",2,"=",hasil)  
# lebih dari sama dengan >= 
print("=============== Lebih dari sama dengan (>=)")
hasil = a >= 3 
print(a,">=",b,"=",hasil) 
hasil = b >= 3 
print(b,">=",3,"=",hasil) 
hasil = b >= 2 
print(b,">=",2,"=",hasil)  
# kurang dari sama dengan <= 
print("=============== Kurang dari sama dengan (<=)") 
hasil = a <= 3 
print(a,"<=",b,"=",hasil)
hasil = b <= 3 
print(b,"<=",3,"=",hasil) 
hasil = b <= 2 
print(b,"<=",2,"=",hasil)  
# sama dengan (==) 
print("=============== Sama dengan (==)") 
hasil = a == 4
print(a,"==",4,"=", hasil)
hasil = b == 4 
print(b,"==",4,"=",hasil)  
# tidak sama dengan (!=) 
print("=============== Tidak sama dengan (!=)") 
hasil = a != 4 
print(a,"!=",4,"=",hasil) 
hasil = b != 4 
print(b,"!=",4,"=",hasil)  
# ‘is’ sebagai komparasi obj identity (bukan literal) 
# x = 5 
# ini adalah assignment membuat object 
# y = 5 
# hasil = x is y 
# print(‘x is y =’,hasil)  
# ‘is not’ sebagai komparasi obj identity (bukan literal) 
# x = 5 
# ini adalah assignment membuat object 
# y = 6 
# hasil = x is not y 
# print(‘x is not y =’,hasil)