# Buat program untuk kondisional if
# Program ini menggunakan fungsi input()
# Progaram menghitung diskon belanja

# input dari user
total_belanja_3011 = float(input("Masukkan Total Belanja (Rp):"))

# input status member (mengecek apakah user mengetik "y" atau "ya")
input_member_3011 = input("Apakah anda member? (y/t)").strip().lower()
is_member_3011 = input_member_3011 in ["y", "ya"]

# input status kode promo 
input_promo_3011 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_3011 = input_promo_3011 in ["y", "ya"]

total_diskon_persen_3011 = 0

# multi-if terpisah
#

if total_belanja_3011 > 1000000:
    total_diskon_persen_3011 += 10 #diskon belanja besar

if is_member_3011:
    total_diskon_persen_3011 += 5 #diskon member

if kode_promo_3011:
    total_diskon_persen_3011 += 15 #diskon promo

#menghitung nominal diskon dan total bayar
nominal_diskon_3011 = total_belanja_3011 * (total_diskon_persen_3011 / 100)
total_bayar_3011 = total_belanja_3011-nominal_diskon_3011

#output hasil
print("\n--- Rincia  Pembayaran---")
print(f"Total Diskon : {total_diskon_persen_3011}% (Rp{nominal_diskon_3011:,.0f})")
print(f"otal_bayar_3011: Rp {total_bayar_3011:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3011}%")