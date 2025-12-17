# Library json untuk manipulasi data/file dengan ekstensi .json, os untuk fungsi clear screen
import json, os

# Nama file yang akan menampung semua data dari program
FILE = "data_mahasiswa.json"

# Membuat file baru jika tidak ada file json
def BuatFile():
    dataKosong = {}

    """
    Pada bagian ini, kita akan membuka file dengan fungsi open() dengan 2 argumen
    yaitu FILE untuk direktori file dan 'w' untuk write/tulis file.
    File tersebut dijadikan sebagai variabel json_file yang dijadikan sebagai
    argumen untuk json.dump().
    json.dump() akan menulis ke dalam file dimana:
    argumen ke-1 adalah datanya
    argumen ke-2 adalah variabel file tadi
    dan argumen ke-3 adalah indentasi sebanyak 4 spasi agar bisa dibaca dengan mudah oleh manusia
    """
    with open (FILE, 'w') as json_file:
        json.dump(dataKosong, json_file, indent=4)

# Mengambil data dari file json, jika nama file yang dicari tidak ada maka akan membuat/generate file secara otomatis
def AmbilData():
    """
    Melakukan pengecekan apakah file dengan lokasi direktori FILE atau data_mahasiswa.json
    Jika ada maka load file dengan fungsi json.load()
    Jika tidak ada maka buat file dengan fungsi BuatFile() dan load filenya
    """
    if os.path.exists(FILE):
        return json.load(open(FILE))
    else:
        BuatFile()
        return json.load(open(FILE))

# Menyimpan data baru ke file data_mahasiswa.json
def SimpanData(data):
    # Menyimpan data ke file dengan argumen 'w' atau menulis data ke dalam file.
    json.dump(data, open(FILE, 'w'), indent=4)

# Menghapus data dari file data_mahasiswa.json
def HapusData(nim, db):
    """
    Menghapus salah satu data pada file data_mahasiswa.json dimana kriterianya adalah nim
    dengan menggunakan del. Setelah itu baru simpan perubahan dengan fungsi SimpanData()
    """
    if nim in db:
        if input(f"Yakin ingin menghapus semua data NIM {nim}? (y/n): ").lower() == 'y':
            del db[nim]
            SimpanData(db)
            input(f"\n[TERHAPUS] Data mahasiswa dengan NIM {nim} telah dihapus dari sistem! Enter...")
    else:
        input(f"\n[GAGAL] NIM {nim} tidak ditemukan, tidak ada yang dihapus. Enter...")

# Menambah data baru ke file data_mahasiswa.json
def TambahData(nim, db):
    if nim not in db:
        """
        Menambah data baru sebagai Dictionary dengan keyword nim dan value awal-nya adalah "NIM_ONLY"
        Lalu simpan penambahan data tersebut ke file data_mahasiswa.json
        """
        db[nim] = "NIM_ONLY"
        SimpanData(db)
        input(f"\n[SUKSES] NIM {nim} berhasil didaftarkan! Enter...")
    else:
        input(f"\n[PERINGATAN] NIM {nim} sudah ada di database! Enter...")

"""
Melakukan cek apakah inputan dengan kriteria nim yang dituju sudah ada
di file data_mahasiswa.json. Jika sudah ada maka masuk ke sub-menu
Biodata untuk nim yang dituju dimana kita bisa mengubah isi biodata,
mencetak isi biodata, ataupun kembali ke menu utama

"""
def CekData(nim, db):
    if nim in db:
        input(f"\n[OK] NIM {nim} ditemukan! Tekan Enter untuk lanjut...")
        while True:
            ClearScreen()
            print(f"----- Menu Biodata NIM: {nim} -----")
            sub = input("1. Isi/Update Biodata\n2. Cek Biodata\n3. Kembali\nPilih: ")

            if sub == '1':
                old = db[nim] if isinstance(db[nim], dict) else {}
                print("\n(Kosongkan/Enter jika data tidak ingin diubah)")
                db[nim] = {
                    "nama": input(f"Nama [{old.get('nama','')}]: ") or old.get('nama',''),
                    "jurusan": input(f"Jurusan [{old.get('jurusan','')}]: ") or old.get('jurusan',''),
                    "prodi": input(f"Program Studi [{old.get('prodi','')}]: ") or old.get('prodi','')
                }
                SimpanData(db)
                input("\n[SUKSES] Biodata telah diperbarui! Enter...")
            elif sub == '2':
                if isinstance(db[nim], dict):
                    print(f"\n----- DATA MAHASISWA -----\nNama\t\t: {db[nim]['nama']}\nJurusan\t\t: {db[nim]['jurusan']}\nProgram Studi\t: {db[nim]['prodi']}")
                else:
                    print("\n[INFO] Biodata masih kosong, silakan isi di menu 1.")
                input("\nTekan Enter untuk kembali...")
            elif sub == '3': break
    else:
        input(f"\n[GAGAL] NIM {nim} tidak ditemukan dalam sistem! Enter...")

# Membersihkan layar terminal
def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'ClearScreen')

# Fungsi utama program untuk menampilkan Menu Utama Data Center kelas 3D
def main():
    db = AmbilData()
    while True:
        ClearScreen()
        print("===== DATA CENTER 3D =====\n1. Cek NIM\n2. Input NIM\n3. Hapus Data\n4. Keluar")
        opt = input("\nPilih Opsi Menu: ")

        if opt == '1':
            nim = input("Masukkan NIM yang dicari: ").upper()
            CekData(nim, db)

        elif opt == '2':
            nim_baru = input("Masukkan NIM Baru: ").upper()
            TambahData(nim_baru, db)

        elif opt == '3':
            nim_hps = input("Masukkan NIM yang akan dihapus: ").upper()
            HapusData(nim_hps, db)

        elif opt == '4':
            print("Keluar dari sistem..."); break

# Melakukan enkapsulasi program python jika dieksekusi langsung, mirip fungsi main class C++ atau Java
if __name__ == "__main__":
    main()