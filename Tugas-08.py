user = input("Masukkan nama anda!")

print(f"\n 🎀 1. Papan catur untuk memasukkan kegiatan {user}🎀")

for baris in range (8):
    for kolom in range (8):
        if (baris + kolom) % 2 == 0:
            print ("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()

print(f"\n 🎀 2. Daftar kegiatan {user}🎀")

Daftar_kegiatan = []
Jumlah_kegiatan = int(input("Berapa jumlah kegiatan yang akan dimasukkan?"))

for i in range (Jumlah_kegiatan):
    print()
    print(f"\n🎀Aktivitas ke-{i+1}🎀")

    Nama_kegiatan = input("Nama kegiatan: ")
    Waktu_kegiatan = input("Waktu kegiatan: ")
    Durasi_kegiatan = input("Durasi kegiatan: ")
    Tempat_kegiatan = input("Tempat kegiatan: ")

    Kegiatan= {
        "Kegiatan": Nama_kegiatan, 
        "Waktu": Waktu_kegiatan,
        "Durasi": Durasi_kegiatan,
        "Tempat": Tempat_kegiatan
    }
    Daftar_kegiatan.append(Kegiatan)
print()

print(f"\n🎀Daftar kegiatan yang telah {user} masukkan🎀")

for i in range(len(Daftar_kegiatan)):
    print(f"Kegiatan {i + 1}")
    print(f"Nama kegiatan : {Daftar_kegiatan[i]['Kegiatan']}")
    print(f"Waktu kegiatan : {Daftar_kegiatan[i]['Waktu']}")
    print(f"Durasi kegiatan : {Daftar_kegiatan[i]['Durasi']}")
    print(f"Tempat kegiatan : {Daftar_kegiatan[i]['Tempat']}")
    print()
