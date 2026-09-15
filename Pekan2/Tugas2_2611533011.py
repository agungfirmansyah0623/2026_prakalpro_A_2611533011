# ==========================================
# SISTEM REGISTRASI PRAKTIKAN ALPRO 2026
# ==========================================

# Konstanta
BATAS_MINIMUM_NILAI = 75.0

# Input data praktikan
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3011 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3011 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3011 = int(input("Masukkan Umur : "))
skor_tes_3011 = float(input("Masukkan Skor Tes Awal : "))


# Data String
alamat_3011 = """Jl. Kampus Unand,
Kecamatan Kuranji,
Kota Padang"""

# Data Complex
id_token_3011 = complex(100, 3)

# Boolean untuk menentukan kelulusan
lulus_3011 = skor_tes_3011 >= BATAS_MINIMUM_NILAI

# ==========================================
# MENAMPILKAN DATA PRAKTIKAN
# ==========================================

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print("Nama Mahasiswa :", nama_3011, "| Tipe:", type(nama_3011))
print("Jenis Kelamin :", jenis_kelamin_3011, "| Tipe:", type(jenis_kelamin_3011))
print("Alamat Domisili:")
print(alamat_3011, "| Tipe:", type(alamat_3011))
print("Umur :", umur_3011, "tahun | Tipe:", type(umur_3011))
print("Skor Tes Awal :", skor_tes_3011, "| Tipe:", type(skor_tes_3011))
print("ID Token Sinyal:", id_token_3011, "| Tipe:", type(id_token_3011))

# ==========================================
# STATUS KELULUSAN
# ==========================================

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

print("Batas Minimum Nilai:", BATAS_MINIMUM_NILAI)
print("Apakah Dinyatakan Lulus?:", lulus_3011, "| Tipe:", type(lulus_3011))