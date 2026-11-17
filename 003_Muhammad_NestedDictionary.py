import datetime 
import os 
import string 
import random
perpustakaan = {
    'judul' : 'judul',
    'penulis' : 'penulis',
    'tahun_terbit':0000,
    'pinjam': datetime.datetime(1111,1,11),
    'status': 'status'
}
info_perpustakaan = {}
while True:    
    os.system("cls" )  
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^95}")  
    print("-"*95)   
    buku = dict.fromkeys(perpustakaan.keys())  
    buku['judul'] = input("JUDUL BUKU\t: ")  
    buku['penulis'] = input("PENULIS\t\t: ")  
    buku['tahun_terbit'] = int(input("TAHUN TERBIT\t: ")) 

    print('\n')
    print(f"{'DATA PEMINJAMAN BUKU':^95}") 
    print("-"*95)
    TAHUN_PINJAM = int(input("Tahun Pinjam (YYYY)\t: "))  
    BULAN_PINJAM = int(input("Bulan Pinjam (1-12)\t: "))  
    TANGGAL_PINJAM = int(input("Tanggal Pinjam (1-31)\t: "))  
    buku['pinjam'] = datetime.datetime(TAHUN_PINJAM,BULAN_PINJAM,TANGGAL_PINJAM)
    status_input = input("\nStatus (TERSEDIA / TIDAK): ").upper()
    buku['status'] = status_input if status_input in ['TERSEDIA', 'TIDAK'] else 'TIDAK'
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))  
    info_perpustakaan.update({KEY:buku})  
    print(f"\n{'KEY':<6} {'JUDUL BUKU':<22} {'PENULIS':<18} {'TERBIT':<8} {'TERAKHIR PINJAM':<17} {'STATUS':<10}")  
    print('-'*95)
    for buku in info_perpustakaan:   
        KEY = buku      
        JUDUL = info_perpustakaan[KEY]['judul']   
        PENULIS = info_perpustakaan[KEY]['penulis']   
        TERBIT = info_perpustakaan[KEY]['tahun_terbit']   
        PINJAM = info_perpustakaan[KEY]['pinjam'].strftime("%x")
        STATUS = info_perpustakaan[KEY]['status'] 
        print(f"{KEY:<6} {JUDUL :<22} {PENULIS:<18} {TERBIT:<8} {PINJAM:<17} {STATUS:<10}")   
    print("\n")  
    is_done = input("Ingin Menambah Buku(y/n)? ")  
    if is_done == "n":   
            break  
print("\nAkhir dari program")