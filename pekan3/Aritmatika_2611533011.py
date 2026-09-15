# buat program untuk operator aritmatika dalam python
# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# nilai yang di masukkan akan di konversi menjadi tipe data integer

angka1_3011 = int(input("input angka-1:"))
angka2_3011 = int(input("input angka-2:"))

# PENJUMLAHAN
hasil = angka1_3011 + angka2_3011
print("\nOperator Penjumlahan")
print("hasil =", hasil)

# PENGURANGAN
hasil = angka1_3011 - angka2_3011
print("\nOperator Pengurangan")
print("hasil =", hasil)

# PERKALIAN
hasil = angka1_3011 * angka2_3011
print("\nOperator Perkalian")
print("hasil =", hasil)

# PEMBAGIAN
if angka2_3011 != 0:
    hasil = angka1_3011 / angka2_3011
    print("\nOperator Pembagian")
    print("hasil =", hasil)

    hasil = angka1_3011 // angka2_3011
    print("\nOperator Pembagian Bulat")
    print("hasil =", hasil)

    hasil = angka1_3011 % angka2_3011
    print("\nOperator Sisa Bagi")
    print("hasil =", hasil)
else:
    print("angka kedua tidak boleh bernilai 0.")

# PANGKAT
hasil = angka1_3011 ** angka2_3011
print("\n Operator Pangkat")
print("hasil =", hasil)
