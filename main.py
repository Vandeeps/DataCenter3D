import json, os

FILE = "data_mahasiswa.json"

def get_data():
    return json.load(open(FILE)) if os.path.exists(FILE) else {}

def save_data(data):
    json.dump(data, open(FILE, 'w'), indent=4)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    db = get_data()
    while True:
        clear()
        print("=== DATA CENTER 3D ===\n1. Cek NIM\n2. Input NIM\n3. Hapus Data\n4. Keluar")
        opt = input("\nPilih Menu: ")

        if opt == '1':
            nim = input("Masukkan NIM yang dicari: ")
            if nim in db:
                input(f"\n[OK] NIM {nim} ditemukan! Tekan Enter untuk lanjut...")
                while True:
                    clear()
                    print(f"--- Menu Biodata NIM: {nim} ---")
                    sub = input("1. Isi/Update Biodata\n2. Cek Biodata\n3. Kembali\nPilih: ")
                    
                    if sub == '1':
                        old = db[nim] if isinstance(db[nim], dict) else {}
                        print("\n(Kosongkan/Enter jika data tidak ingin diubah)")
                        db[nim] = {
                            "nama": input(f"Nama [{old.get('nama','')}] : ") or old.get('nama',''),
                            "jurusan": input(f"Jurusan [{old.get('jurusan','')}] : ") or old.get('jurusan',''),
                            "prodi": input(f"Prodi [{old.get('prodi','')}] : ") or old.get('prodi','')
                        }
                        save_data(db)
                        input("\n[SUKSES] Biodata telah diperbarui! Enter...")
                    elif sub == '2':
                        if isinstance(db[nim], dict):
                            print(f"\n--- DATA MAHASISWA ---\nNama: {db[nim]['nama']}\nJurusan: {db[nim]['jurusan']}\nProdi: {db[nim]['prodi']}")
                        else:
                            print("\n[INFO] Biodata masih kosong, silakan isi di menu 1.")
                        input("\nTekan Enter untuk kembali...")
                    elif sub == '3': break
            else:
                input(f"\n[GAGAL] NIM {nim} tidak ditemukan dalam sistem! Enter...")

        elif opt == '2':
            nim_baru = input("Masukkan NIM Baru: ")
            if nim_baru not in db:
                db[nim_baru] = "NIM_ONLY"
                save_data(db)
                input(f"\n[SUKSES] NIM {nim_baru} berhasil didaftarkan! Enter...")
            else: 
                input(f"\n[PERINGATAN] NIM {nim_baru} sudah ada di database! Enter...")

        elif opt == '3':
            nim_hps = input("Masukkan NIM yang akan dihapus: ")
            if nim_hps in db:
                if input(f"Yakin ingin menghapus semua data NIM {nim_hps}? (y/n): ").lower() == 'y':
                    del db[nim_hps]
                    save_data(db)
                    input(f"\n[TERHAPUS] Data mahasiswa dengan NIM {nim_hps} telah dihapus dari sistem! Enter...")
            else:
                input(f"\n[GAGAL] NIM {nim_hps} tidak ditemukan, tidak ada yang dihapus. Enter...")

        elif opt == '4': 
            print("Keluar dari sistem..."); break

if __name__ == "__main__":
    main()