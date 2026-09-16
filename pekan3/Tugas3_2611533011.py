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
print(f"Total Belanja                      :  Rp{total_belanja_3011}")
print("Jumlah Barang                      : ", jumlah_barang_3011)
print("Kode Promo                         : ", promo_3011)

#=========================================
#=========HASIL VALIDASI================
#=========================================

kode_promo_3011 = ["HIDUP IF", "HIDUP FTI", "JALAN SEHAT"]


print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000                : {total_belanja_3011 >= 200000}") 
print(f"Jumlah Barang >= 3                 : {jumlah_barang_3011 >= 3}")
print(f"Status Member                      : {status_3011 == "member"}")
print(f"Kode Promo Tersedia                : {promo_3011 in kode_promo_3011}")
print(f"Mendapatkan Diskon                 : {promo_3011 in kode_promo_3011}")
print(f"Mendapatkan Promo                  : {promo_3011 in kode_promo_3011}")

#=========================================
#  =====HASIL PERHITUNGAN============
#=========================================

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                             : Rp{int(0.15 * total_belanja_3011)}")
print(f"Total Pembayaran                   : Rp{int(total_belanja_3011 - 0.15 * total_belanja_3011)}")
print(f"Rata-rata Harga Barang             : Rp{int((total_belanja_3011 - 0.15 * total_belanja_3011) // jumlah_barang_3011)}")

#=========================================
#=========HAK AKSES PELANGGAN===========
#=========================================
 
print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses                     : ...")
print(f"Member Access                      : {status_3011 == "member"}")
print(f"Promo Access                       : {promo_3011 in kode_promo_3011}")
print("Free Shipping Access               : ...")

#=========================================
#=========OPERASI BITWISE===============
#=========================================


print("\n=== OPERASI BITWISE ===")

print("\n=== Kode Status Transaksi ===")

#KODE STATU
#0001 = member
#0010 = Belom di pakai
#0100 = Belom di pakai
#1000 = promo

#menggunakan OR (|)
kode_member_3011 = 0b0001
kode_promo_3011 = 0b1000
kode_status_3011 = ( kode_member_3011 | 0b0010 | 0b0100 | kode_promo_3011)



print("0001 | 0010 | 0100 | 1000")
print("Kode Biner   : ", format(kode_status_3011, "04b"))
print("Kode Desimal : ", kode_status_3011)


#====================================
#========PEMERIKSAAN STATUS=========
#====================================

print("\n=== Pemeriksaan Status ===")


print("\nCek Member")

#menggunakan and (&)

cek_member_3011 = kode_status_3011 & kode_member_3011
cek_promo_3011 = kode_status_3011 & kode_promo_3011

print("1111 & 0001")
print("Hasil Biner   :", format(cek_member_3011, "04b"))
print("Hasil Desimal :", cek_member_3011)

print("\nCek Promo")

print("1111 & 1000")
print("Hasil Biner   :", format(cek_promo_3011, "04b"))
print("Hasil Desimal :", cek_promo_3011)


#====================================
#======PERBANDINGAN STATUS==========
#============================================

print("\n=== Perbandingan Status ===")


 # menggunakan XOR (^)


kode_referensi_3011 = 0b1011
hasil_XOR_3011 = kode_status_3011 ^ kode_referensi_3011

print("Kode Transaksi :", format(kode_status_3011, "04b"))
print("Kode Referensi :", format(kode_referensi_3011, "04b"))

print("1111 ^ 1011")

print("Hasil Biner   :", format(hasil_XOR_3011, "04b"))
print("Hasil Desimal :", hasil_XOR_3011)

#=====================================
#=======SHIFT GESER KIRI=============
#=====================================


print("\n=== Shift ===")

#bitwise kiri/ shift kiri (<<)

hasil_shift_3011 = kode_status_3011 << 1

print("1111 << 1")
print("Hasil Biner   :", format(hasil_shift_3011, "b"))
print("Hasil Desimal :", hasil_shift_3011)

print("\n=== SELESAI ===")