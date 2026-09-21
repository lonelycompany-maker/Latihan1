print("=== Kasir Kantin V2 ===")
total_belanja = 0

while True:
    input_harga = input("Masukkan harga barang (ketik 'selesai' untuk total): ")

    if input_harga == "selesai":
        # 1. Tulis perintah rem darurat (break) di sini:
        break
        
    # 2. Tambahkan harga ke total_belanja (Ingat Casting ke Integer!)
    # Petunjuk: total_belanja = total_belanja + int(input_harga)
    total_belanja = total_belanja + int(input_harga)

print("Total Belanja Anda: Rp " + str(total_belanja))