# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# program operator perbandingan dalam python

angka1_3011 = int(input("input angka-1:"))
angka2_3011 = int(input("input angka-2:"))

# Lebih besar dari
hasil = angka1_3011 > angka2_3011
print("\n Operator lebih besar dari")
print("angka1 > angka 2 =", hasil)

# Lebih kecil dari
hasil = angka1_3011 < angka2_3011
print("\n Operator lebih kecil dari")
print("angka1 < angka 2 =", hasil)

# Lebih besar dari atau sama dengan
hasil = angka1_3011 >= angka2_3011
print("\n Operator lebih besar dari atau sama dengan")
print("angka1 >= angka 2 =", hasil)

# Lebih kecil dari atau sama dengan
hasil = angka1_3011 <= angka2_3011
print("\n Operator lebih kecil dari atau sama dengan")
print("angka1 <= angka 2 =", hasil)

#  Sama dengan
hasil = angka1_3011 == angka2_3011
print("\n Operator sama dengan")
print("angka1 == angka 2 =", hasil)

# tidak sama dengan
hasil = angka1_3011 != angka2_3011
print("\n Operator tidak sama dengan")
print("angka1 != angka 2 =", hasil)

# Tambahan: perbandingan berarti dalam python
hasil = 0 < angka1_3011 < 100
print("\n Perbandingan berantai")
print("0 < angka1 < 100 =", hasil)

hasil = 0 < angka2_3011 < 100
print("0 < angka2 < 100 =", hasil)
