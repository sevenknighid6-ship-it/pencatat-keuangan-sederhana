# 💰 Aplikasi Pencatat Keuangan Sederhana

Aplikasi ini dibuat menggunakan **Python** untuk membantu mencatat **pemasukan dan pengeluaran uang** secara sederhana melalui terminal.

---

## 🚀 Fitur Utama
- Menambahkan transaksi baru (pemasukan / pengeluaran)
- Melihat daftar seluruh transaksi
- Menampilkan total saldo akhir
- Validasi input agar tidak terjadi kesalahan

---

## 🧠 Alur Program (Pseudocode)

Mulai
Tampilkan menu utama:
  1. Tambah transaksi
  2. Lihat transaksi
  3. Keluar
Jika pilih 1:
  Masukkan jenis (pemasukan/pengeluaran)
  Masukkan jumlah uang
  Masukkan keterangan
  Simpan ke daftar transaksi
Jika pilih 2:
  Tampilkan semua transaksi
  Hitung saldo akhir
Jika pilih 3:
  Tampilkan pesan keluar
Selesai

---

## 🧾 Kode Program (Python)

```python
# Aplikasi Pencatat Keuangan Sederhana

transaksi = []

def tambah_transaksi():
    print("\n=== Tambah Transaksi ===")
    jenis = input("Jenis (pemasukan/pengeluaran): ").lower()
    if jenis not in ["pemasukan", "pengeluaran"]:
        print("Jenis tidak valid!")
        return
    jumlah = float(input("Masukkan jumlah uang: "))
    keterangan = input("Keterangan: ")
    transaksi.append({"jenis": jenis, "jumlah": jumlah, "keterangan": keterangan})
    print("Transaksi berhasil ditambahkan!")

def lihat_transaksi():
    print("\n=== Daftar Transaksi ===")
    if not transaksi:
        print("Belum ada transaksi.")
        return
    total_masuk = sum(t["jumlah"] for t in transaksi if t["jenis"] == "pemasukan")
    total_keluar = sum(t["jumlah"] for t in transaksi if t["jenis"] == "pengeluaran")
    saldo = total_masuk - total_keluar
    for i, t in enumerate(transaksi, start=1):
        print(f"{i}. {t['jenis'].capitalize()} - Rp{t['jumlah']} ({t['keterangan']})")
    print("---------------------------")
    print(f"Saldo akhir: Rp{saldo}")

def menu():
    while True:
        print("\n=== Menu Pencatat Keuangan ===")
        print("1. Tambah transaksi")
        print("2. Lihat transaksi")
        print("3. Keluar")
        pilih = input("Pilih menu (1/2/3): ")
        if pilih == "1":
            tambah_transaksi()
        elif pilih == "2":
            lihat_transaksi()
        elif pilih == "3":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid!")

menu()
```

---

## 🧪 Uji Manual
| Jenis Uji | Input | Output yang Diharapkan |
|------------|--------|-------------------------|
| Tambah pemasukan | pemasukan, 100000, “Gaji” | Transaksi tersimpan |
| Tambah pengeluaran | pengeluaran, 50000, “Makan” | Transaksi tersimpan |
| Lihat transaksi | - | Menampilkan daftar dan saldo akhir Rp50000 |
| Input jenis salah | “tabungan” | Muncul pesan “Jenis tidak valid!” |

---

## 🛠️ Cara Menjalankan
1. Pastikan Python sudah terinstal (`python --version`)
2. Simpan file ini sebagai `pencatat_keuangan.py`
3. Jalankan melalui terminal:
   ```bash
   python pencatat_keuangan.py
   ```

---

## 📦 Struktur Folder
```
📂 Pencatat-Keuangan
 ┣ 📜 pencatat_keuangan.py
 ┗ 📜 README.md
```

---

## 💡 Ide Pengembangan
- Menyimpan data transaksi ke file `.txt` atau `.csv`
- Menambahkan tanggal transaksi otomatis
- Tampilan GUI sederhana dengan Tkinter

---

✍️ **Dibuat oleh:** [Nama Kamu]  
📅 **Tahun:** 2025
