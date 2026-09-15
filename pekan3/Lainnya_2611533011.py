print("======================")
print(" 1. OPERATOR KEANGGOTAAN")
print("======================")

# input beberapa data yang dipisahkan dengan koma
input_data = input("masukkan beberapa angka, pisahkan dengan koma: ")

# mengubah input menjadi list integer
data = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("masukkan angka yang ingin di cari: "))

#operator in 
hasil = nilai_dicari in data 
print("\n Operator keanggotaan IN")
print(nilai_dicari, "in", data, "=", hasil)

# operator not in 
hasil = nilai_dicari not in data 
print("\n Operator keanggotaan NOT IN")
print(nilai_dicari, "not in", data, "=", hasil)

# ke skip







# membandingkan identitas dan nilai 
print("\n perbandingan identitas dan nilai")
print("objek is objek3 =", objek1 is objek3)
