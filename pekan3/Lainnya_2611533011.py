print("======================")
print(" 1. OPERATOR KEANGGOTAAN")
print("======================")

# input beberapa data yang dipisahkan dengan koma
input_data_3011 = input("masukkan beberapa angka, pisahkan dengan koma: ")

# mengubah input menjadi list integer
data_3011 = [int(angka.strip()) for angka in input_data_3011.split(",")]

nilai_dicari_3011 = int(input("masukkan angka yang ingin di cari: "))

#operator in 
hasil_3011 = nilai_dicari_3011 in data_3011 
print("\n Operator keanggotaan IN")
print(nilai_dicari_3011, "in", data_3011, "=", hasil_3011)

# operator not in 
hasil_3011_3011 = nilai_dicari_3011 not in data_3011 
print("\n Operator keanggotaan NOT IN")
print(nilai_dicari_3011, "not in", data_3011, "=", hasil_3011)


print("\n===========================")
print("2. OPERATOR IDENTITAS")
print("===========================")

# objek1 menggunakan list dari input pengguna 
objek1_3011 = data_3011

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3011 = objek1_3011 

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3011 = data_3011.copy()

print("objek1_3011 =", objek1_3011)
print("objek2_3011 =", objek2_3011)
print("objek3_3011 =",objek3_3011)

# operator is
hasil_3011= objek1_3011 is objek2_3011
print("\n Operator identitas IS")
print("objek1_3011 is objek2_3011 =", hasil_3011)

# operator is not
hasil_3011 = objek1_3011 is objek3_3011
print("\n Operator identitas IS NOT")
print("objek1_3011 is not objek3_3011 =", hasil_3011)

# membandingkan identitas dan nilai 
print("\n membandingkan identitas dan nilai")
print("objek1_3011 is objek3_3011: ", objek1_3011 is objek3_3011)
print("objek1_3011 == objek3_3011: ", objek1_3011 == objek3_3011)