# Aplikasi Pencatat Keuangan Sederhana
\
transaksi = []\
\
def tambah_transaksi():\
    print("\\n=== Tambah Transaksi ===")\
    jenis = input("Jenis (pemasukan/pengeluaran): ").lower()\
    if jenis not in ["pemasukan", "pengeluaran"]:\
        print("Jenis tidak valid!")\
        return\
    jumlah = float(input("Masukkan jumlah uang: "))\
    keterangan = input("Keterangan: ")\
    transaksi.append(\{"jenis": jenis, "jumlah": jumlah, "keterangan": keterangan\})\
    print("Transaksi berhasil ditambahkan!")\
\
def lihat_transaksi():\
    print("\\n=== Daftar Transaksi ===")\
    if not transaksi:\
        print("Belum ada transaksi.")\
        return\
    total_masuk = sum(t["jumlah"] for t in transaksi if t["jenis"] == "pemasukan")\
    total_keluar = sum(t["jumlah"] for t in transaksi if t["jenis"] == "pengeluaran")\
    saldo = total_masuk - total_keluar\
    for i, t in enumerate(transaksi, start=1):\
        print(f"\{i\}. \{t['jenis'].capitalize()\} - Rp\{t['jumlah']\} (\{t['keterangan']\})")\
    print("---------------------------")\
    print(f"Saldo akhir: Rp\{saldo\}")\
\
def menu():\
    while True:\
        print("\\n=== Menu Pencatat Keuangan ===")\
        print("1. Tambah transaksi")\
        print("2. Lihat transaksi")\
        print("3. Keluar")\
        pilih = input("Pilih menu (1/2/3): ")\
        if pilih == "1":\
            tambah_transaksi()\
        elif pilih == "2":\
            lihat_transaksi()\
        elif pilih == "3":\
            print("Terima kasih telah menggunakan aplikasi!")\
            break\
        else:\
            print("Pilihan tidak valid!")\
\
menu()\
}