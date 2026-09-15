# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()


print("\n========================================")
print("3. Operator Bitwise")
print("==========================================")

angka1_3011 = int(input("Masukkan angka bitwise-1: "))
angka2_3011 = int(input("masukkan angka bitwise-2: "))

print("\n angka dalam bentuk desimal dan biner")
print("angka1 =", angka1_3011, "| biner = ", bin(angka1_3011))
print("angka2 =", angka2_3011, "| biner = ", bin(angka2_3011))

# Bitwise AND
hasil_3011 = angka1_3011 & angka2_3011
print("\n Bitwise AND (&)")
print(angka1_3011, "&", angka2_3011, "=", hasil_3011)
print("Biner Hasil =", bin (hasil_3011))
print("Biner Hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise OR
hasil_3011 = angka1_3011 | angka2_3011
print("\n Bitwise OR (|)")
print(angka1_3011, "|", angka2_3011, "=", hasil_3011)
print("Biner Hasil =", bin(hasil_3011))
print("Biner Hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise XOR
hasil_3011 = angka1_3011 ^ angka2_3011
print("\n Bitwise XOR (^)")
print(angka1_3011, "^", angka2_3011, "=", hasil_3011)
print("Biner Hasil", bin(hasil_3011))
print("Biner Hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise NOT
hasil_3011 = ~angka1_3011
print("\n Bitwise NOT (~)")
print("~", angka1_3011, "=", hasil_3011)
print("Biner Hasil", bin(hasil_3011))
print("Biner Hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\n masukkan jumlah pergeseran bit: "))

hasil_3011 = angka1_3011 << jumlah_geser
print("\n Bitwise geser kiri (<<)")
print(angka1_3011, "<<", jumlah_geser, "=", hasil_3011)
print("Biner Hasil", bin(hasil_3011))
print("Biner Hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise geser kanan
hasil_3011 = angka1_3011 >> jumlah_geser
print("\n Bitwise geser kanan (>>)")
print(angka1_3011, ">>", jumlah_geser, "=", hasil_3011)
print("Biner Hasil", bin(hasil_3011))
print("Biner Hasil (8 bit) =", format(hasil_3011, "08b"))
