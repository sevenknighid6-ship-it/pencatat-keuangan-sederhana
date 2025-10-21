{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Aplikasi Pencatat Keuangan Sederhana\
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