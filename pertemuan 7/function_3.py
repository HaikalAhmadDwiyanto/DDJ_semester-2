def berangkat_sekolah(pakaian, buku):
    if pakaian == "seragam" and buku == "bawa":
        print("berangkat sekolah")
    else:
        print("pergi main")

def nama_siswa(nama):
    print(nama)

print(nama_siswa("murti"), berangkat_sekolah("seragam", "bawa"))
print(nama_siswa("sugri"), berangkat_sekolah("jeans", "tidak membawa buku"))
print(nama_siswa("budi"), berangkat_sekolah("seragam", "tidak membawa buku"))