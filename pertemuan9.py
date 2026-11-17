# import datetime
# mahasiswa1 = {  
#     'nama':'Ash Blosom',  
#     'nim' :'19022001',  
#     'sks_lulus':130, 
#     'beasiswa': False,  
#     'lahir':datetime.datetime(2001,4,10) # tahun, tanggal, bulan 
#     }   
# mahasiswa2 = {  
#     'nama':'Nibiru',  
#     'nim' :'19022002',  
#     'sks_lulus':140 , 
#     'beasiswa':True ,  
#     'lahir':datetime.datetime(2002,10,10) # tahun, tanggal, bulan 
#     }   
# mahasiswa3 = {  
#     'nama':'Doomz',  
#     'nim' :'19022003',  
#     'sks_lulus':100 , 
#     'beasiswa':True,  
#     'lahir':datetime.datetime(1977,5,10) # tahun, tanggal, bulan 
#     }  
# data_mahasiswa = {  
#     ('MAH001'):mahasiswa1,  
#     ('MAH002'):mahasiswa2,  
#     ('MAH003'):mahasiswa3, 
#     } 
# print(f'{'KEY':<6} {'Nama':<12} {'SKS':<7} {'Beasiswa':<11} {'Lahir':<10}')  
# print('-'*50)  
# for mahasiswa in data_mahasiswa:     
#     KEY = mahasiswa          
#     NAMA = data_mahasiswa[KEY]['nama']     
#     NIM = data_mahasiswa[KEY]['nim']     
#     SKS = data_mahasiswa[KEY]['sks_lulus']     
#     BEASISWA = data_mahasiswa[KEY]['beasiswa']     
#     LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')      
#     print(f'{KEY:<6} {NAMA:<12} {SKS:<8} {BEASISWA:<9} {LAHIR:<10}') 
# print('\n')

# import datetime  
# mahasiswa_template = {      
#     'nama':'nama',  
#     'nim':00000000,  
#     'sks_lulus':0,  
#     'lahir':datetime.datetime(1111,1,11) 
#     }  
# data_mahasiswa = {}  
# print(f'{'SELAMAT DATANG':^20}') 
# print(f'{'DATA MAHASISWA':^20}') 
# print('-'*20)  
# mahasiswa = dict.fromkeys(mahasiswa_template.keys()) 
# print(mahasiswa) 
# mahasiswa['nama'] = input('Nama Mahasiswa: ') 
# mahasiswa['nim'] = input('NIM Mahasiswa: ') 
# mahasiswa['sks_lulus'] = int(input('SKS Lulus')) 
# TAHUN_LAHIR = int(input('Tahun lahir (YYYY): ')) 
# BULAN_LAHIR = int(input('Bulan lahir (1-12): ')) 
# TANGGAL_LAHIR = int(input('Tanggal lahir (1-31): ')) 
# mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)  
# print(mahasiswa)   
# print('\n')

import datetime 
import os 
import string 
import random  # template dict mahasiswa 
mahasiswa_template = {  
    'nama':'nama',  
    'nim':'00000000',  
    'sks_lulus':0,  
    'lahir':datetime.datetime(1111,1,11) 
    }  
data_mahasiswa = {}  
while True:  
    # os.system("cls") # untuk windows  
    os.system("cls")  
    print(f"{'SELAMAT DATANG':^60}")  
    print(f"{'DATA MAHASISWA':^60}")  
    print("-"*60)   
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())  
    mahasiswa['nama'] = input("Nama Mahasiswa: ")  
    mahasiswa['nim'] = input("NIM Mahasiswa: ")  
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))  
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))  
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))  
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))  
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)   
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))  
    data_mahasiswa.update({KEY:mahasiswa})   # dari program sebelumnya, hilangkan beasiswa  
    print(f"\n{'KEY':<6} {'Nama':<12} {'NIM':<10} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")  
    print('-'*60)   
    for mahasiswa in data_mahasiswa:   
        KEY = mahasiswa      
        NAMA = data_mahasiswa[KEY]['nama']   
        NIM = data_mahasiswa[KEY]['nim']   
        SKS = data_mahasiswa[KEY]['sks_lulus']   
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")      
        print(f"{KEY:<6} {NAMA:<10} {NIM:<8} {SKS:^14} {LAHIR:^10}")   
    print("\n")  
    is_done = input("Mau tambah lagi bro (y/n)? ")  
    if is_done == "n":   
            break  
print("\nAkhir dari program, terima kasih")

# import datetime

# mahasiswa1 = {"nama": "Dragoon", "sks_lulus": 130, "lahir": datetime.datetime(2001, 4, 10)}
# mahasiswa2 = {"nama": "Bistyal", "sks_lulus": 140, "lahir": datetime.datetime(2002, 10, 10)}
# mahasiswa3 = {"nama": "Star", "sks_lulus": 100, "lahir": datetime.datetime(1977, 5, 10)}

# data_mahasiswa = {
#     ("MAH001"): mahasiswa1,
#     ("MAH002"): mahasiswa2,
#     ("MAH003"): mahasiswa3,
# }

# for key, mhs in data_mahasiswa.items():
#     lahir = mhs["lahir"].strftime("%d-%m-%Y")
#     print(f"{key}: {mhs['nama']} sudah lulus {mhs['sks_lulus']} SKS dan lahir pada {lahir}.")
# print(f"{'KEY':<6} | {'Nama':<20} | {'SKS':<3} | {'Lahir':<30}")
# print("-" * 68)

# for key, mhs in data_mahasiswa.items():
#     format_lahir = mhs['lahir'].strftime("tanggal %d bulan %m tahun %Y")
#     print(f"{key:<6} | {mhs['nama']:<20} | {mhs['sks_lulus']:<3} | {format_lahir:<30}")

# mahasiswa = {}

# mahasiswa["nama"] = input("Nama Mahasiswa: ")
# mahasiswa["nim"] = input("NIM Mahasiswa: ")
# mahasiswa["jurusan"] = input("Jurusan: ")

# print(mahasiswa)
# data_mahasiswa = {}

# while True:
#     mahasiswa = {}

#     nama = input("Nama: ")
#     jenis_kelamin = input("Jenis kelamin: ")
#     npm = int(input("NPM: "))

#     mahasiswa["nama"] = nama
#     mahasiswa["jenis_kelamin"] = jenis_kelamin

#     print(mahasiswa)

#     # Simpan ke data mahasiswa
#     data_mahasiswa[npm] = mahasiswa

#     lagi = input("Tambah lagi (y/n)? ")
#     if lagi == "n":
#         break

# print("Selesai")
# # Tampilkan semua data Mahasiswa
# print(data_mahasiswa)