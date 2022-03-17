masa_kerja = int(input("Masa Kerja : "))
umur = int(input("Umur : "))
if masa_kerja >= 5:
    if umur >50:
        print("Anda Mendapatkan bonus 20%")
    else:
        print("Anda Mendapatkan bonus 10%")
else:
    print("Maaf anda belum beruntung cuy")