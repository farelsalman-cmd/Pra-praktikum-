# print("Nama saya Farel")

# program 2.2
# variabel adalah tempat menyimpan data
# tipe data 

# 1. String = karakter 
# 2. Integer = bilangan bulat
# 3. double / float = bilangan desimal 
# 4. boolean = menampung true / false

# tipe data pada python

#x = 5
#y = 10

#print(x)
#print("Nilai y adalah",y)

# aturan penamaan
#nilai_y = 15        # Menggunakan underscore
#juta10 = 10000000   # Tidak boleh diawali angka
#nilaiz = 17.5       # Camel case   

#print("nilai y", nilai_y)  # pemanggilan ke 1
#nilai_y = 10
#print("nilai y", nilai_y)  # pemanggilan ke 2

#program 2.3
#data integer
data_integer = 1
print("data_integer :", data_integer)
print("- bertipe ", type(data_integer))
print("\n")
#data float
data_float = 7.7
print("data float :", data_float)
print("bertipe ", type(data_float))
print("\n")
#data string
data_string = "Farel"
print("data string :", data_string)
print("bertipe ", type(data_string))
print("\n")
#data bool
data_bool = True
print("data bool :", data_bool)
print("bertipe", type(data_bool))
print("\n")
#data complex
data_complex = complex(5,6)
print("data :", data_complex)
print("bertipe", type(data_complex))
print("\n")
#type data dari bahasa c
#from ctype import c_double
#data_c_double = c_double(10.5)
#print("data :", data_c_double)
#print("bertipe", type(data_c_double))

#program 2.4
#INT ke data lain
data_int = 9

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))
print("\n")
#FLOAT ke data lain
data_float = 9.2

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))
print("\n")
#STR ke data lain
data_str = "10"

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_bool, ", type = ", type(data_bool))

#program 2.5
#input data user

#data yang dimasukan pasti string
data = input("Masukan data: ")
print("data",data,",type =", type(data))
print("\n")
#jika ingin mengambil int, maka
angka = int(input("Masukan angka: "))
print("data",angka,",type =", type(angka))