# Buat program untuk kondisional if
# Program ini menggunakan fungsi input()

umur_3011 = int(input("Input umur anda: "))
sim_3011 = input("Apakah anda sudah punya Sim C (y/t): ")[0]

if umur_3011 >= 17 and sim_3011 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")

elif umur_3011 >= 17 and sim_3011 != "y":
    print("Anda suda dewasa tetapi tidak boleh bawa motor")

elif umur_3011 < 17 and sim_3011 =="y":
    print("Anda belum cukup umur dan punya SIM")

else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program selesai")