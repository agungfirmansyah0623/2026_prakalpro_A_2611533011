# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# program operator assignment dalam python

angka1_3011 = int(input("input angka-1: "))
angka2_3011 = int(input("input angka-1: "))

print("\n nilai awal angka1 =", angka1_3011)
print("nilai angka2 =", angka2_3011)

# assignment biasa 
hasil = angka1_3011
print("\n assingmnet biasa (=)")
print("hasil =", hasil)

# assignment penambahan
hasil = angka1_3011
hasil += angka2_3011
print("\n assignment penambahan (+=)")
print("hasil =", hasil)

# assignment perkalian
hasil = angka1_3011
hasil *= angka2_3011
print("\n assignment perkalian (*=)")
print("hasil =", hasil)

# assignment pembagian, pembagian bulat, dan sisa bagi 
if angka2_3011 != 0:
    hasil = angka1_3011
    hasil /= angka2_3011
    print("\n assignment pembagian (/=)")
    print("hasil =", hasil)

    #operator tambahan
    hasil = angka1_3011
    hasil //= angka2_3011
    print("\n assignment pembagian bulat (//=)")
    print("hasil =", hasil)

    hasil = angka1_3011
    hasil %= angka2_3011
    print("\n assignment sisa bagi (%=)")
    print("hasil =", hasil)

else:
    print("\n pembagian tidak dapat dilakukan")
    print("angka kedua tidak boleh 0")