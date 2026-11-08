# 1. Tuple
# a. membuat data tuple
print('='*31, 'Soal No 1 Tuple', '='*32)
mahasiswa = ('Nama','NPM','Prodi')
print(mahasiswa, '\n')
# b. menampilkan data tuple dengan menyebutkan index
print(mahasiswa[1])
print(mahasiswa[2], '\n')
## c. menjalankan kode tuple dengan merubah data suatu index, menjelaskan kenapa terjadi error pada kode tersebut
# mahasiswa[2]= 'Teknologi Informasi'
# print(mahasiswa[2])
# tuple merupakan salah satu kode yang elemen pada suatu index nya tetap 
# dan tidak dapat dirubah,ditambah,dikurangi, maupun dihapus. Jika dirubah seperti contoh diatas maka akan terjadi error
## d. membuat sebuah set
nilai_angka={ 10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)
# saat kita print, jika terdapat pada data set terdapat suatu elemen yang dan lebih dari satu
# maka elemen tersebut hanya akan dicetak ulang satu kali atau yang muncul hanya satu
# seperti contoh di atas, angka 10 dan 4 masing masing terdapat satu pasang, namun ketika di cetak hanya satu elemen yang muncul.
print('='*80,'\n')

# 2. Manipulasi Dictionary
print('='*20, 'Soal No 2 Manipulasi Dictionary', '='*27)
# a. membuat dictionary
data_mahasiswa = {
  "nim": "240101" ,
  "nama": "Budi Santoso",
  "prodi": "Teknologi Informasi"
}
print('Data Awal Mahasiswa :')
print('Data Mahasiswa :',data_mahasiswa)
# b. merubah nilai 'prodi' menjadi sastra mesin
print('Data Mahasiswa setelah dirubah :')
data_mahasiswa['prodi']= 'Sastra Mesin'
print('Data Mahasiswa :',data_mahasiswa)
# c. menghapus data 'nim'
print('Data Akhir Mahasiswa :')
del data_mahasiswa['nim']
print('Data Mahasiswa :',data_mahasiswa)
print('='*80,'\n')

# 3. Perulangan Dictionary
print('='*20, 'Soal No 3 Perulangan Dictionary', '='*27)
# a. Data Dictionary
keranjang = {
    "apel": 5000, 
    "pisang": 3000, 
    "jeruk": 7000, 
    "anggur": 15000,
}
print(keranjang,'\n')
# b. Perulangan untuk menampilkan informasi barang
for key,value in keranjang.items():
    print(f'Harga {key} \t: Rp{value}')
print('\n')
# c. Total Belanja
total = 0
for h,i in keranjang.items():
    total += i
#total = sum(keranjang.values())
print(f'Harga Total \t: Rp{total}')
print('='*80,'\n')