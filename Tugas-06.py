from datetime import datetime

print("hi! selamat sore")
print("ini menu nya, silahkan dilihat-lihat dulu ya!")
print("sarapan")
print("pergi bekerja")

aktivitas = input ("pilih aktivitas yang ingin kamu lakukan ya!")

if aktivitas.lower() == "sarapan":

    print("ini untuk menu nya, silahkan dipilih terlebih dahulu ya")
    print("telur")
    print("ikan")
    print("nugget")

    menu = input ("mau sarapan dengan menu apa hari ini?")

    if menu.lower()== "telur" or menu.lower () =="ikan" or menu.lower()== "nugget":
        print (f"baik, {menu} tersedia. harap dimasak dahulu ya!")
    else:
        print (f"wah, sebelum itu kamu harus membeli bahannya terlebih dahulu")

elif aktivitas.lower() == "pergi kerja":
    waktu = datetime.now()
    print("jam 08.00 pagi, waktu kamu pergi kerja ya")
    print(f"sekarang sudah pukul {waktu}")

    if waktu.hour < 08.00:
         print("wow, masih ada waktu luang, jadi bisa olahraga terlebih dahulu ya!")
    elif waktu.hour == 08.00:
        print("sudah jam 08.00 nih, lain kali lebih awal ya agar tidak terburu-buru")
    else:
        print("duh, kamu sudah terlambat, kedepannya usahakan bangun dan bersiap lebih pagi ya!")