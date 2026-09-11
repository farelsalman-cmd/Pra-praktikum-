#program yang meminta user memasukkan usia seseorang, lalu kategorikan usia tersebut
print('===========================================\n\tKategori Berdasarkan Usia\n===========================================')
usia = int(input('Berapa Umur Anda? '))
if usia == usia>=0 and usia<=12:
    print('Kategori Anak-anak')
else:
    print('Bukan Kategori Anak-anak')
if usia == usia>=13 and usia<=17:
    print('Kategori Remaja')
else:
    print('Bukan Kategori Remaja')
if usia == usia>=18 and usia<=59:
    print('Kategori Dewasa')
else:
    print('Bukan Kategori Dewasa')
if usia == usia>=60:
    print('Kategori Lansia')
else:
    print('Bukan Kategori Lansia')
print('===========================================')