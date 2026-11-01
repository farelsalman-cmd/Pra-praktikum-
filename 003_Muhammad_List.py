#Soal No 1
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
kendaraan.append('truk')
print(f'kendaraan ditambah lagi = \n{kendaraan}')
kendaraan.insert(1,'becak')
print(f'kendaraan sesudah ditambahkan = \n{kendaraan}')
kendaraan.remove('bus')
print(f'kendaraan akhir dihapus = \n{kendaraan}')
kendaraan[2] = 'skuter'
print(f'kendaraan dirubah = \n{kendaraan}')
jkendaraan = len(kendaraan)
print(f'jumlah kendaraan = {jkendaraan}')
print('\n')
#Soal No 2
angka= [75, 80, 90, 75, 85, 100, 65]
indexangka= angka.index(100)
print(f'Index angka 100 = {indexangka}')
nilai = angka.count(75)
print(f'banyak nilai 75 = {nilai}')
angka.sort()
print(f'urutan nilai dari terendah = {angka}')
angka.reverse()
print(f'urutan nilai dari tertinggi = {angka}')
print('\n')
#Soal No 3
menu_utama = ["Nasi Goreng", "Mie Ayam"] 
menu_tambahan = ["Kerupuk", "Es Teh"]
menu_gabungan = ['Menu Utama',menu_utama,'Menu Tambahan',menu_tambahan]
print(f'Keseluruhan Menu = {menu_gabungan}')
print('\n')
#Soal No 4
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
print(f'Informasi barang : {data_barang[1]} \n')
for barang in data_barang:
    print(f'Nama barang\t : {barang[0]}')
    print(f'Harga barang\t : {barang[1]} \n')