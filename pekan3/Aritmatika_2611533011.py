# buat program untuk operator aritmatika dalam python
# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# nilai yang di masukkan akan di konversi menjadi tipe data integer

angka1_3011 = int(input("input angka-1:"))
angka2_3011 = int(input("input angka-2:"))

# PENJUMLAHAN
hasil_3011 = angka1_3011 + angka2_3011
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3011)

# PENGURANGAN
hasil_3011 = angka1_3011 - angka2_3011
print("\nOperator Pengurangan")
print("Hasil =", hasil_3011)

# PERKALIAN
hasil_3011 = angka1_3011 * angka2_3011
print("\nOperator Perkalian")
print("Hasil =", hasil_3011)

# PEMBAGIAN
if angka2_3011 != 0:
    hasil_3011 = angka1_3011 / angka2_3011
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3011)

    hasil_3011 = angka1_3011 // angka2_3011
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3011)

    hasil_3011 = angka1_3011 % angka2_3011
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3011)
else:
    print("angka kedua tidak boleh bernilai 0.")

# PANGKAT
hasil_3011 = angka1_3011 ** angka2_3011
print("\n Operator Pangkat")
print("Hasil=", hasil_3011)
