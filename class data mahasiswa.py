class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

class DaftarNilaiMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, nama, nilai):
        mahasiswa = Mahasiswa(nama, nilai)
        self.mahasiswa_list.append(mahasiswa)

    def tampilkan_daftar(self):
        if not self.mahasiswa_list:
            print("Daftar mahasiswa kosong.")
            return

        print("Daftar Nilai Mahasiswa:")
        for idx, mahasiswa in enumerate(self.mahasiswa_list, start=1):
            print(f"{idx}. {mahasiswa.nama} - Nilai: {mahasiswa.nilai}")

    def hapus_mahasiswa(self, nama):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nama == nama:
                self.mahasiswa_list.remove(mahasiswa)
                print(f"Mahasiswa dengan nama '{nama}' berhasil dihapus.")
                return
        print(f"Mahasiswa dengan nama '{nama}' tidak ditemukan.")

    def ubah_data_mahasiswa(self, nama):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nama == nama:
                print(f"Data ditemukan untuk mahasiswa '{nama}'.")
                mahasiswa.nama = input("Masukkan nama baru: ")
                try:
                    mahasiswa.nilai = float(input("Masukkan nilai baru: "))
                    print("Data mahasiswa berhasil diubah.")
                except ValueError:
                    print("Nilai harus berupa angka!")
                return
        print(f"Mahasiswa dengan nama '{nama}' tidak ditemukan.")

# Program utama
daftar_nilai = DaftarNilaiMahasiswa()

while True:
    print("\nMenu:")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Daftar Mahasiswa")
    print("3. Hapus Mahasiswa")
    print("4. Ubah Data Mahasiswa")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        try:
            nilai = float(input("Masukkan nilai mahasiswa: "))
            daftar_nilai.tambah_mahasiswa(nama, nilai)
            print("Mahasiswa berhasil ditambahkan!")
        except ValueError:
            print("Nilai harus berupa angka!")
    elif pilihan == "2":
        daftar_nilai.tampilkan_daftar()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        daftar_nilai.hapus_mahasiswa(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang datanya ingin diubah: ")
        daftar_nilai.ubah_data_mahasiswa(nama)
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
