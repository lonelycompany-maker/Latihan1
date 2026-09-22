daftar_tugas = []

def tambah_tugas(nama_tugas):
    # 1. Gunakan .append() untuk memasukkan nama_tugas ke daftar_tugas
    daftar_tugas.append(nama_tugas)
    print("Sukses ditambahkan!")

def tampilkan_tugas():
    print("--- DAFTAR TUGASMU ---")
    for t in daftar_tugas:
        print("- " + t)

# Memanggil fungsi (Menggunakan mesinnya)
tambah_tugas("Belajar Python Sesi 9")
tambah_tugas("Mengerjakan Kuis")

# 2. Panggil fungsi tampilkan_tugas di baris bawah ini:
tampilkan_tugas()