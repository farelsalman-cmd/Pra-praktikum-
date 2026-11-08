# # LIST
# # menggunakan kurung siku
# data_list = [10,2,4,3,2]
# print(data_list)
# # tuples
# data_tuples = (7,8,10,11,7)
# print(data_tuples)
# print(data_tuples[1])
# tidak bisa dilakukan
# data_tuples[1] = 'ucup'
# data_tuples.append(1)
# print(data_tuples)
# # sets (himpunan)
# data_sets = {10,4,3,2,3}
# print(data_sets)
# print(data_sets[2])
# print('\n')

# ## Dictionary
# # list → array, mengakses dengan menggunakan index
# data_list = ['Ash','Baron','Rikka']
# print(data_list[0])
# # dictionary (dict) → associative array
# # identifier → key
# data_dict = {
#  'ht':'nibiru',
#  'ss': 'nova',
#  'tc': 'star',
#  'sc': 'monica',
#  'nmbr': 100,
#  'list': data_list
# }
# print(data_dict['ht'])
# print(data_dict['nmbr'])
# print(data_dict['list'])
# print('\n')
# ## --- Operasi Dictionary ---
# data_dict = {
# 'ht':'Ash Blossom',
# 'nc':'El Stratos',
# 'sc':'Polymer'
# }
# # panjang dictionary
# LENDICT = len(data_dict)
# print(f'panjang dictionary: {LENDICT}')
# # mengecek key exist atau tidak
# KEY = 'ht'
# CHECKKEY = KEY in data_dict
# print(f'apakah {KEY} ada di data_dict: {CHECKKEY}')
# # mengakses value (read) dengan get
# print(data_dict['ht'])
# print(data_dict.get('ht'))
# print(data_dict.get('kis','key tidak ditemukan')) # check key dengan message
# # mengupdate data
# data_dict['ht'] = 'Maximum C'
# print(data_dict)
# data_dict['fs'] = 'Sunrise'
# print(data_dict)
# data_dict.update({'ht':'Fuwaloss'})
# print(data_dict)
# data_dict.update({'tc':'Foolish'}) # akan di tambah jika tidak ada
# print(data_dict)
# # menghapus data
# del data_dict['tc']
# print(data_dict)
# print('\n')
## --- Looping Dictionary ---
kartu_anak = {
 'ht':'Veiler',
 'trap':'Solemn',
 'spel':'Droplet',
 'bum':'Nibiru' 
}
# looping first try (yang keluar hanya key)
for card in kartu_anak:
 print(card)
# operator untuk mengambil item
keys = kartu_anak.keys()
print(keys)
for key in kartu_anak.keys():
 print(kartu_anak.get(key))
values = kartu_anak.values()
print(values)
for value in kartu_anak.values():
 print(value)
items = kartu_anak.items()
print(items)
for item in kartu_anak.items():
 print(item)
for key,value in kartu_anak.items():
 print(f'key = {key}, value = {value}')