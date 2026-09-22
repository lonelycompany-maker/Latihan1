def hitung_diskon(harga, persen):
    potongan = harga * (persen / 100)
    # UBAH KATA print DI BAWAH INI MENJADI return
    return potongan

harga_baju = 100000
diskonnya = hitung_diskon(harga_baju, 20)

harga_akhir = harga_baju - diskonnya
print("Harga yang harus dibayar: Rp " + str(harga_akhir))