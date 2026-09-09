is_lulus = True
is_cumlaude = True

nilai_3011 = 85
batas_lulus = 75

status_kelulusan = nilai_3011 >= batas_lulus
print("=== Check Kelulusan ===")
print("Nilai:" , nilai_3011)
print("Apakah lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")