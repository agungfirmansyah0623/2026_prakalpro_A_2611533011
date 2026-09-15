# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# program operator assignment dalam python

angka1_3011 = int(input("input angka-1: "))
angka2_3011 = int(input("input angka-1: "))

print("\n nilai awal angka1 =", angka1_3011)
print("nilai angka2 =", angka2_3011)

# assignment biasa 
hasil_3011 = angka1_3011
print("\n assingmnet biasa (=)")
print("Hasil =", hasil_3011)

# assignment penambahan
hasil_3011 = angka1_3011
hasil_3011 += angka2_3011
print("\n assignment penambahan (+=)")
print("Hasil =", hasil_3011)

# assignment perkalian
hasil_3011 = angka1_3011
hasil_3011 *= angka2_3011
print("\n assignment perkalian (*=)")
print("Hasil =", hasil_3011)

# assignment pembagian, pembagian bulat, dan sisa bagi 
if angka2_3011 != 0:
    hasil_3011 = angka1_3011
    hasil_3011 /= angka2_3011
    print("\n assignment pembagian (/=)")
    print("Hasil =", hasil_3011)

    #operator tambahan
    hasil_3011 = angka1_3011
    hasil_3011 //= angka2_3011
    print("\n assignment pembagian bulat (//=)")
    print("Hasil =", hasil_3011)

    hasil_3011 = angka1_3011
    hasil_3011 %= angka2_3011
    print("\n assignment sisa bagi (%=)")
    print("Hasil =", hasil_3011)

else:
    print("\n pembagian tidak dapat dilakukan")
    print("angka kedua tidak boleh 0")