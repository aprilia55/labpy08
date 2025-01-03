Nama : Alfarizki Aprilia Putri 

NIM : 312410455

Kelas : TI.24.A5

# Praktikum 8 - class untuk menampilkan daftar nilai mahasiswa 

Program ini dibuat untuk mengelola data mahasiswa beserta nilai mereka. Program ini menggunakan konsep Object-Oriented Programming (OOP) dengan memanfaatkan class untuk merepresentasikan data mahasiswa dan pengelolaan daftar nilai. Program ini dirancang untuk memberikan fitur-fitur berikut:

**Menambahkan data mahasiswa**

**Menampilkan daftar mahasiswa dan nilai mereka**

**Menghapus data mahasiswa berdasarkan nama**

**Menghitung rata-rata nilai mahasiswa**

**Struktur Program**

**Class** `Mahasiswa`

Class ini digunakan untuk merepresentasikan data individual mahasiswa.

**Atribut:**

`nama`: Nama mahasiswa.

`nilai`: Nilai mahasiswa.

```python
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
```
`__init__ `: Konstruktor yang menerima parameter nama dan nilai untuk menginisialisasi atribut mahasiswa.

**Class** `Daftar Nilai Mahasiswa`

Class ini digunakan untuk mengelola daftar mahasiswa.

**Atribut**:

`mahasiswa_list`: List yang menyimpan objek-objek dari class `Mahasiswa`.

Metode:

1. **`tambah_mahasiswa(nama, nilai)`**

Menambahkan objek mahasiswa baru ke dalam daftar.

Parameter:

`nama`: Nama mahasiswa (string).

`nilai`: Nilai mahasiswa (float).

```python
def tambah_mahasiswa(self, nama, nilai):
    mahasiswa = Mahasiswa(nama, nilai)
    self.mahasiswa_list.append(mahasiswa)
```

2. **`tampilkan_daftar()`**

Menampilkan semua data mahasiswa dalam format terstruktur.

Jika daftar kosong, akan mencetak pesan "Daftar mahasiswa kosong."

```python
def tampilkan_daftar(self):
    if not self.mahasiswa_list:
        print("Daftar mahasiswa kosong.")
        return

    print("Daftar Nilai Mahasiswa:")
    for idx, mahasiswa in enumerate(self.mahasiswa_list, start=1):
        print(f"{idx}. {mahasiswa.nama} - Nilai: {mahasiswa.nilai}")
```

3.**`hapus_mahasiswa(nama)`**

Menghapus data mahasiswa berdasarkan nama.

Parameter:

`nama`: Nama mahasiswa yang ingin dihapus (string).

Jika nama tidak ditemukan, akan mencetak pesan "Mahasiswa dengan nama '[nama]' tidak ditemukan."

```python
def hapus_mahasiswa(self, nama):
    for mahasiswa in self.mahasiswa_list:
        if mahasiswa.nama == nama:
            self.mahasiswa_list.remove(mahasiswa)
            print(f"Mahasiswa dengan nama '{nama}' berhasil dihapus.")
            return
    print(f"Mahasiswa dengan nama '{nama}' tidak ditemukan.")
```

4.**` Mengubah Data Mahasiswa`**

Kode menu nomor 4 sekarang digunakan untuk mengubah data mahasiswa. Metode ubah_data_mahasiswa mencari mahasiswa berdasarkan nama, lalu meminta input nama dan nilai baru jika ditemukan. Jika nama tidak ada atau input nilai tidak valid, program menampilkan pesan yang sesuai. 

```python
elif pilihan == "4":
    nama = input("Masukkan nama mahasiswa yang datanya ingin diubah: ")
    daftar_nilai.ubah_data_mahasiswa(nama)
```
Dan pastikan metode berikut ada di kelas `DaftarNilaiMahasiswa`:

```python
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
```
python
Salin kode


**Cara Menggunakan**

Menjalankan Program:

Jalankan program menggunakan interpreter Python.

Program akan menampilkan menu pilihan untuk interaksi pengguna.

**Menu Program:**

**1. Tambah Mahasiswa:**

Masukkan nama mahasiswa.

Masukkan nilai mahasiswa (format angka/desimal).

Data mahasiswa akan ditambahkan ke dalam daftar.

**2. Tampilkan Daftar Mahasiswa:**

Menampilkan semua data mahasiswa dan nilai mereka.

**3. Hapus Mahasiswa:**

Masukkan nama mahasiswa yang ingin dihapus.

Jika mahasiswa ditemukan, datanya akan dihapus.

Jika tidak ditemukan, pesan kesalahan akan ditampilkan.

4.**Mengubah data Nama**

Menghitung data (Nama) Mahasiswa.

**5. Keluar:**

Mengakhiri program.

# Contoh diagram kode program
![foto](https://github.com/aprilia55/labpy08/blob/e37d9e22872e7b24373ed9af05ac2b528d5f082b/Screen%20Shot%202024-12-10%20at%2023.03.44.png)
# Hasil Interaksi Program
![foto](https://github.com/aprilia55/labpy08/blob/664f3cf048368536bf56ef1c0e523c9c31600387/Screen%20Shot%202024-12-10%20at%2022.34.37.png)
# flowchart alur program
![foto](https://github.com/aprilia55/labpy08/blob/ef54baab814d727cc344dbedff6c1280dd38da73/flowchart%20alur%20program.jpeg)
