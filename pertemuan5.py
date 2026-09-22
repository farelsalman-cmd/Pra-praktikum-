#Perulangan

#angka=1
#print(angka)
#angka=angka+1
#print(angka)
#angka=angka+1
#print(angka)
#print('\n')

#forkondisi:
#aksi  #dengan 
#list 
#angka2 = [0,1,2,3,4] 
# ini adalah list 
#print(angka2)  
#print('\n')
#for i in angka2:  
# print(i) 
#print(f) -> kombinasi text dan variabel 
#print('akhiri dari program \n')  
#dengan range 
#angka3 = range(5)  
#for i in angka3:   
# print(i) 
#print('akhiri dari program\n')

#angka4 = range(1,5) 
#for i in angka4:   
#  print(i)  
  #print(“Jedarrr”) 
 # print('akhiri dari program\n') 
  
# menggunakan string 
#data_str = 'Cihuyyy'  
#for huruf in data_str:  
 #print(huruf) 
 #print('akhiri dari program\n')
#program

# while loop  
#while kondisi: 
# aksi ini # aksi itu   
print('===contoh 1===')  
angka = 10 
while angka > 5:
  angka = angka - 1
  print('Duarrr')  
print('\n')
print('===contoh 2===')  
angka = 5
while angka <= 5:  
 #angka + 1  
  angka = angka - 1  
  if(angka==0):
   print('Sut')  
   break
  print('Duar')  
print('akhiri program')
print('\n')
# continue, pass, break  
#pass → dia berfungsi sebagai dummy, tidak akan dieksekusi  
angka = 0  
while angka < 5:  
  angka = angka + 1    
  if(angka == 3):
     pass # ini tidak akan dieksekusi  
  print(angka)  
print("\n")
#continue  
angka = 0 
print(f'angka sekarang → {angka}')  
while angka < 5:  
  angka = angka + 1  
  print('angka sekarang →', angka) # aksi 1   
  if(angka == 3): 
    print('angka sekarang →', angka) 
    continue   # akan membuat loop meloncat ke step selanjutnya  
  print('Eyyoo') # aksi 2  
print('End')
print('\n')
# break  
angka = 0 
print(f'angka sekarang → {angka}') 
while angka < 5:  
  angka = angka + 1  
  print(f'angka sekarang → {angka}') # aksi 1   
  if(angka == 3):   
    print('Sure')   
    break  
  print('Helloo') # aksi 2  
print('OFF')
print('\n')
#latihan membuat segitiga 
# 1. Menggunakan for 
sisi = 10
count = 1
for i in range(sisi): 
  print('*' * count) 
  count += 1  
print('\n')

# 2. Menggunakan while 
sisi = 7
count = 1
while True:
  print('*' * count) 
  count += 1 
  if count > sisi:
    break