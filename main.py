import json, os

FILE = "data_mahasiswa.json"

def AmbilData():
    return json.load(open(FILE)) if os.path.exists(FILE) else {}

def SimpanData(data):
    json.dump(data, open(FILE, 'w'), indent=4)

def HapusData(nim, db):
    if nim in db:
        if input(f"Yakin ingin menghapus semua data NIM {nim}? (y/n): ").lower() == 'y':
            del db[nim]
            SimpanData(db)
            input(f"\n[TERHAPUS] Data mahasiswa dengan NIM {nim} telah dihapus dari sistem! Enter...")
    else:
        input(f"\n[GAGAL] NIM {nim} tidak ditemukan, tidak ada yang dihapus. Enter...")

def TambahData(nim, db):
    if nim not in db:
        db[nim] = "NIM_ONLY"
        SimpanData(db)
        input(f"\n[SUKSES] NIM {nim} berhasil didaftarkan! Enter...")
    else:
        input(f"\n[PERINGATAN] NIM {nim} sudah ada di database! Enter...")

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

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'ClearScreen')

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

if __name__ == "__main__":
    main()