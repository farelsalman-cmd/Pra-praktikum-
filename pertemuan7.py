# --- LIST ---
#Kumpulan data numbers 
data_angka = [1,5,2,3] 
print(data_angka)
# Kumpulan data_string
data_string = ['ucup','adit','siti'] 
print(data_string)
# Kumpulan data boolean
data_boolean = [True, False, True, True] 
print(data_boolean)
# Kumpulan campuran
data_campuran = [1,'bakwan',2,'cireng','ucup',True,'adit',False] 
print(data_campuran)
print('\n')
# cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step) 
print(data_range)
data_list = list(data_range) 
print(data_list)
print('\n')
# membuat list dengan for loop, list comprehension
list_for = [i **2 for i in range(0,10)] 
print(list_for)
# membuat list pake for pake if
list_for_if = [i for i in range(0,10) if i !=5] 
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 != 0] 
print(list_for_if)
print('\n')
## --- Operasi LIST ---
# index 0(-3)1(-2)2(-1)
data = ['Ucup','Adit','Dadang']
# mengambil data dari list 
data_0 = data[0]
print(f'data pertama (index 0) = {data_0}')
data_terakhir = data[-1]
print(f'data terakhir adalah = {data_terakhir}')
# mengambil info jumlah data dalam list 
panjang_data = len(data) 
print(f'panjang data = {panjang_data}')
print('\n')
# manipulasi data list
# menambahkan item pada list sesuai posisi 
print(f'data sebelum ditambah = \n{data}')
#data.insert(posisi,item)
data.insert(1,'Asep')
print(f'data sesudah ditambah= \n{data}')
# menambah di akhir list 
data.append('Ririn')
print(f'data ditambah lagi = \n{data}')
# menambahkan list dengan list 
data_baru = ['Luffy','Zoro','Nami'] 
data.extend(data_baru)
print(f'data gabungan = \n{data}')
#merubah data
# kita ubah data 2 menjadi jarwo 
data[2] = 'jarwo'
print(f'data rubah = \n{data}')
# menghapus data 
data.remove('Ucup')
print(f'data hapus = \n{data}')
# menghapus data paling belakang 
data.pop()
print(f'data akhir = \n{data}')
print('\n')
## --- Operasi LIST ---
# index 0(-3)1(-2)2(-1)
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f'data angka = \n{data_angka}') 
# count data
jumlah_data_4 = data_angka.count(4) 
jumlah_data_3 = data_angka.count(3)
print(f'jumlah angka 4 = {jumlah_data_4}') 
print(f'jumlah angka 3 = {jumlah_data_3}')
# ambil posisi data
data = ['Rendi','Iqbal','Gana','Khairil'] 
print(f'data = {data}')
index_Iqbal = data.index('Iqbal') 
index_Gana = data.index('Gana')
print(f'index si Iqbal = {index_Iqbal}') 
print(f'index si Gana = {index_Gana}')
# mengurutkan list
print(f'data angka sebelum sort = \n {data_angka}') 
data_angka.sort()
print(f'data angka sort = \n{data_angka}')
      
print(f'data = {data}') 
data.sort()
print(f'data sort = {data}')
# balik listnya 
data_angka.reverse() 
data.reverse()
print(f'data di reverse \n{data_angka}') 
print(f'data di reverse \n{data}')
print('\n')
## --- Nested LIST ---
data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print(f'list biasa = {data_list_biasa}')
list_2D = [data_0, data_1, 6,7] 
print(f'list 2D = {list_2D}')
# contoh penggunaan
peserta_0 = ['Rendi', 25, 'Laki-laki'] 
peserta_1 = ['Joni', 10, 'Laki-laki'] 
peserta_2 = ['Eka', 50, 'Wanita']
list_peserta = [peserta_0, peserta_1, peserta_2] 
print(f'peserta = {list_peserta}')
print('\n')
for peserta in list_peserta: 
 print(f'Nama\t : {peserta[0]}')
 print(f'Umur\t : {peserta[1]}') 
 print(f'Gender\t : {peserta[2]}\n')