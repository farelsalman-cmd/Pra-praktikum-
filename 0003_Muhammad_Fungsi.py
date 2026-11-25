# Buatlah program dengan input dan fungsi untuk menghitung: 
# a. Luas persegi panjang 
print(f"{'Luas Persegi Panjang':^40}")
print("=" * 40)
def Luas_PersegiPanjang (panjang,lebar):
    panjang= int(input('Panjang\t = '))
    lebar= int(input('Lebar\t = '))
    luas = panjang*lebar
    return luas
Luas= Luas_PersegiPanjang ('panjang','lebar')
print('Luas Persegi Panjang =',Luas)
print("=" * 40)
print('\n')
# b. Volume persegi panjang
print(f"{'Volume Persegi Panjang':^40}")
print("=" * 40)
def Volume_Balok (panjang,lebar,tinggi):
    panjang= int(input('Panjang\t = '))
    lebar= int(input('Lebar\t = '))
    tinggi=int(input('Tinggi\t = '))
    volume = panjang*lebar*tinggi
    return volume
Volume= Volume_Balok ('panjang','lebar','tinggi')
print('Volume Balok =',Volume) 
print("=" * 40)
print('\n')
# c. Luas lingkaran 
print(f"{'Luas lingkaran':^40}")
print("=" * 40)
def Luas_Lingkaran (jari_jari,phi):
    jari_jari= int(input('Jari-jari\t = '))
    if jari_jari% 7 == 0:
        phi= 22/7
        print("Phi\t\t = 22/7")
    else :
        phi = 3.14
        print("Phi\t\t = 3.14")
    Luas = phi * jari_jari**2
    print('Luas Lingkaran\t = phi * jari_jari**2')
    return Luas
LuasL= Luas_Lingkaran ('jari_jari','phi')
print('Luas Lingkaran\t = ', LuasL)
print("=" * 40)
print('\n')
# d. Volume bola
print(f"{'Volume bola':^40}")
print("=" * 40)
def Volume_Bola (jari_jari,phi):
    jari_jari= int(input('Jari-jari\t = '))
    if jari_jari% 7 == 0:
        phi= 22/7
        print("Phi\t\t = 22/7")
    else :
        phi = 3.14
        print("Phi\t\t = 3.14")
    Volume = 4/3* phi * jari_jari**3
    print('Volume Bola\t = 4/3 * phi * jari_jari**3')
    return Volume
VolumeB= Volume_Bola ('jari_jari','phi')
print('Volume Bola\t = ', VolumeB)
print("=" * 40)