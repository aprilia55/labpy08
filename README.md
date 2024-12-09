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

4. **`hitung_rata_rata()`**

Menghitung dan mencetak rata-rata nilai dari semua mahasiswa dalam daftar.

Jika daftar kosong, akan mencetak pesan "Tidak ada data mahasiswa untuk dihitung rata-rata."

```python
def hitung_rata_rata(self):
    if not self.mahasiswa_list:
        print("Tidak ada data mahasiswa untuk dihitung rata-rata.")
        return

    total_nilai = sum(mahasiswa.nilai for mahasiswa in self.mahasiswa_list)
    rata_rata = total_nilai / len(self.mahasiswa_list)
    print(f"Rata-rata nilai: {rata_rata:.2f}")
```

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

**4. Hitung Rata-rata Nilai:**

Menghitung rata-rata nilai dari semua mahasiswa dalam daftar.

**5. Keluar:**

Mengakhiri program.

# Contoh Interaksi Program
![foto]()



