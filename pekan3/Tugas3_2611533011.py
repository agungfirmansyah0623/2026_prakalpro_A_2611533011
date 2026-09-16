print ("\n=== SISTEM TRANSAKSI TOKO ===")

nama_3011 = input("Masukkan Nama Pelanggan: ")
status_3011 = input("Masukkan Status Pelanggan (member/nonmember): ")
total_belanja_3011 = int(input("Masukkan Total Belanja : "))
jumlah_barang_3011 = int(input("Masukkan Jumlah Barang : "))
promo_3011 = input("Masukkan Kode Promo : ")

 #========================================
 #  ======DATA TRANSAKSI======
 # =======================================


print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan                     : ",nama_3011)
print("Status Pelanggan (member/nonmember): ", status_3011)
print(f"Total Belanja                     : Rp{total_belanja_3011}")
print("Jumlah Barang                      : ", jumlah_barang_3011)
print("Kode Promo                         : ", promo_3011)

#=========================================
#=========HASIL VALIDASI================
#=========================================

kode_promo_3011 = ["HEMAT10", "HEMAT20", "GRATIS ONGKIR"]


print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000               : Rp{total_belanja_3011 >= 200000}") 
print(f"Jumlah Barang >= 3                : {jumlah_barang_3011 >= 3}")
print(f"Status Member                     : {status_3011 == "member"}")
print(f"Kode Promo Tersedia               : {promo_3011 in kode_promo_3011}")
print(f"Mendapatkan Diskon                : {promo_3011 in kode_promo_3011}")
print(f"Mendapatkan Promo                 : {promo_3011 in kode_promo_3011}")

#=========================================
#  =====HASIL PERHITUNGAN============
#=========================================

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                            : {4000 * total_belanja_3011}")
print(f"Total Pembayaran                  : {total_belanja_3011 - total_belanja_3011 * 4000}")
print(f"Rata-rata Harga Barang            : {total_belanja_3011 // total_belanja_3011 *4000}")

 
print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses                     : ...")
print(f"Member Access                     : {status_3011 == "member"}")
print(f"Promo Access                      : {promo_3011 in kode_promo_3011}")
print("Free Shipping Access               : ...")

print("\n=== OPERASI BITWISE ===")

print("\n=== Kode Status Transaksi ===")

0001 | 0010 | 0100 | 1000

Kode Biner   : 1111

Kode Desimal : 15

=== Pemeriksaan Status ===

Cek Member

1111 & 0001

Hasil Biner   : 0001

Hasil Desimal : 1

 

Cek Promo

1111 & 1000

Hasil Biner   : 1000

Hasil Desimal : 8

=== Perbandingan Status ===

Kode Transaksi : 1111

Kode Referensi : 1011

1111 ^ 1011

Hasil Biner   : 0100

Hasil Desimal : 4

=== Shift ===

1111 << 1

Hasil Biner   : 11110

Hasil Desimal : 30 

=== SELESAI ===