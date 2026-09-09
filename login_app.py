user = input("Username: ")
pw = input("Password: ")

# Ganti tanda tanya (?) dengan Logika and
if user == "admin" and pw == "telkom123":
    print("Login Berhasil! Selamat Datang Admin.")
else: 
    print("Login Gagal. Username atau Password salah")