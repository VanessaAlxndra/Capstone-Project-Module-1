#CAPSTONE PROJECT MODULE 1
#Nama : Vanessa Alexandra
#No : JCDS-2804-014

from tabulate import tabulate
import pwinput
from datetime import datetime

listBarang = {
    1: {'Nama Barang' : 'Lemari Pakaian', 'Stok' : 10, 'Qty Terjual' : 5, 'Harga Beli':700000,'Harga Jual': 900000, 'Kategori': 'Bedroom', 'Warna' : 'Brown', 'Batch No' : 'JAN122025', 'Waktu Masuk': '2025-02-16 17:23:32', 'Waktu Keluar': ''},
    2: {'Nama Barang' : 'Sofa', 'Stok' : 10, 'Qty Terjual' : 2,'Harga Beli': 3500000,'Harga Jual': 5000000, 'Kategori': 'Living Room', 'Warna' : 'Black', 'Batch No' : 'FEB142025',  'Waktu Masuk': '2025-02-16 17:23:32', 'Waktu Keluar': ''},
    3: {'Nama Barang' : 'Meja Makan', 'Stok' : 10, 'Qty Terjual' : 0,'Harga Beli': 350000, 'Harga Jual': 500000, 'Kategori': 'Dining Room', 'Warna' : 'White',  'Batch No' : 'DES162025', 'Waktu Masuk': '2025-02-16 17:23:32', 'Waktu Keluar': ''},
    4: {'Nama Barang' : 'Kursi Makan', 'Stok' : 10, 'Qty Terjual' : 0,'Harga Beli': 150000, 'Harga Jual': 200000, 'Kategori': 'Dining Room', 'Warna' : 'White',  'Batch No' : 'DES162025', 'Waktu Masuk': '2025-02-16 17:23:32', 'Waktu Keluar': ''},
    5: {'Nama Barang' : 'Tempat Tidur', 'Stok' : 10, 'Qty Terjual' : 0,'Harga Beli': 4500000, 'Harga Jual': 6000000, 'Kategori': 'Bedroom', 'Warna' : 'Grey',  'Batch No' : 'JAN122025', 'Waktu Masuk': '2025-02-16 17:23:32', 'Waktu Keluar': ''},
    6: {'Nama Barang' : 'Rak Buku', 'Stok' : 10, 'Qty Terjual' : 3,'Harga Beli': 200000, 'Harga Jual': 250000, 'Kategori': 'Bedroom', 'Warna' : 'Brown',  'Batch No' : 'OKT122025', 'Waktu Masuk': '2025-02-16 17:23:32', 'Waktu Keluar': ''},
    7: {'Nama Barang' : 'Kabinet', 'Stok' : 10, 'Qty Terjual' : 2,'Harga Beli': 1100000, 'Harga Jual': 1250000, 'Kategori': 'Living Room', 'Warna' : 'Black',  'Batch No' : 'OKT122025', 'Waktu Masuk': '2025-02-16 17:23:32', 'Waktu Keluar': ''},
    8: {'Nama Barang' : 'Meja Tamu', 'Stok' : 10, 'Qty Terjual' : 1,'Harga Beli': 250000, 'Harga Jual': 300000, 'Kategori': 'Living Room', 'Warna' : 'Grey',  'Batch No' : 'OKT122025', 'Waktu Masuk': '2025-02-16 17:23:32', 'Waktu Keluar': ''}
}

def daftarBarang(listBarang):
    idBarang = [{'ID Barang': index, **item} for index, (key, item) in enumerate(listBarang.items(), start=1)]
    table = tabulate(idBarang, headers='keys', tablefmt='grid', maxcolwidths=[5, 5, 5, 8, 8, 10, 5, 5, 5, 5])
    print("\n Daftar Barang:")
    print(table)

def tambahBarang(listBarang):
    daftarBarang(listBarang)
    namaBaru = input("Masukkan Nama Barang: ").title()
    stokBaru = int(input("Masukkan Stok Barang: "))
    hargaBaru = int(input("Masukkan Harga Beli: "))
    kategoriBaru = input("Masukkan Kategori Barang: ")
    warnaBaru = input("Masukkan Warna Barang: ")
    batchNoBaru = input("Masukkan Batch No Barang: ")

    idBaru = max(listBarang.keys()) + 1
    listBarang[idBaru] = {
        'Nama Barang': namaBaru,
        'Stok': stokBaru,
        'Qty Terjual': 0,  # Set Qty Terjual awal ke 0
        'Harga Beli': hargaBaru,
        'Harga Jual': 0,  # Set harga jual awal ke 0
        'Kategori': kategoriBaru,
        'Warna': warnaBaru,
        'Batch No': batchNoBaru,
        'Waktu Masuk': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Waktu Keluar': ''
    }
    daftarBarang(listBarang)

def kurangBarang(listBarang):
    daftarBarang(listBarang)
    hapusID = int(input("Masukkan ID Barang yang ingin dihapus: "))
    if hapusID in listBarang:
        del listBarang[hapusID]
    else:
        print("ID tidak valid!")
    daftarBarang(listBarang)

def updateBarang(listBarang):
    daftarBarang(listBarang)
    idUpdate = int(input("Masukkan ID Barang yang ingin diupdate: "))
    if idUpdate not in listBarang:
        print("ID tidak valid!")
        return
    while True:
        print(''' 
                Pilih informasi barang yang ingin diupdate:
              1. Nama Barang
              2. Stok Barang
              3. Harga Beli
              4. Kategori
              5. Warna
              6. Batch No
              ''')
        revisi = input("Masukkan informasi barang yang ingin diupdate (1-5): ")

        if revisi == "1":
            namaAfter = input("Masukkan nama baru barang: ")
            listBarang[idUpdate]['Nama Barang'] = namaAfter
        elif revisi == "2":
            stokAfter = int(input("Masukkan stok baru barang: "))
            listBarang[idUpdate]['Stok'] = stokAfter
        elif revisi == "3":
            hargaAfter = int(input("Masukkan harga baru barang: "))
            listBarang[idUpdate]['Harga Beli'] = hargaAfter
        elif revisi == "4":
            kategoriAfter = input("Masukkan kategori baru barang: ")
            listBarang[idUpdate]['Kategori'] = kategoriAfter
        elif revisi == "5":
            warnaAfter = input("Masukkan warna baru barang: ")
            listBarang[idUpdate]['Warna'] = warnaAfter
        elif revisi == "6":
            batchNoAfter = input("Masukkan batch no barang: ")
            listBarang[idUpdate]['Batch No'] = batchNoAfter
        else:
            print("Pilihan Anda tidak valid!")
            continue
        daftarBarang(listBarang)
        break

def hargaBarang(listBarang):
    daftarBarang(listBarang)
    idBarang = int(input("Masukkan ID Barang untuk mengatur harga jual: "))
    if idBarang in listBarang:
        hargaJual = int(input("Masukkan harga jual barang: "))
        listBarang[idBarang]['Harga Jual'] = hargaJual
        print("Harga jual berhasil diupdate.")
    else:
        print("ID barang tidak valid!")
    daftarBarang(listBarang)

def alokasiBarang(listBarang):
    daftarBarang(listBarang)
    idBarang = int(input('Masukkan ID Barang yang terjual: '))
    if idBarang in listBarang:
        qtyTerjual = int(input("Masukkan Qty Barang Terjual: "))
        if qtyTerjual <= listBarang[idBarang]['Stok']:
            listBarang[idBarang]['Stok'] -= qtyTerjual # Mengurangi stok barang
            listBarang[idBarang]['Qty Terjual'] += qtyTerjual # Update Qty Terjual
            listBarang[idBarang]['Waktu Keluar'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Update Waktu Keluar
            print("Data barang terjual berhasil diupdate.")
            daftarBarang(listBarang)
        else:
            print("Stok tidak cukup untuk qty yang diminta.")
    else:
        print("ID barang tidak valid!")

while True:
    print('''
          Halo, silakan login terlebih dahulu!
          ''')
    username = input("Masukkan username Anda: ")
    password = pwinput.pwinput()

    if username == "admin" and password == "admin01":
        while True:
            print('''
                  Selamat Datang di Gudang Furniture
                  \n
                  List Menu:
                  1. Menampilkan Daftar Barang
                  2. Menambah Barang 
                  3. Menghapus Barang
                  4. Mengupdate Barang
                  5. Exit Program
                  ''')
            pilihan = input("Masukkan angka Menu yang ingin dijalankan: ")
            
            if pilihan == "1": # Menampilkan Daftar Barang
                daftarBarang(listBarang)
            elif pilihan == "2": # Menambah Barang
                tambahBarang(listBarang)
            elif pilihan == "3": # Menghapus Barang
                kurangBarang(listBarang)
            elif pilihan == "4": #Mengupdate Informasi Barang
                updateBarang(listBarang)
            elif pilihan == "5": # Exit Program
                print("Terima kasih telah menggunakan program ini!")
                break
            else:
                print("Pilihan tidak valid! Silakan pilih menu 1-5.")

    elif username == "marketing" and password == "marketing02":
        while True:
            print('''
                  Selamat Datang di Gudang Furniture
                  \n
                  List Menu:
                  1. Menampilkan Daftar Barang
                  2. Menentukan Harga Jual Barang 
                  3. Mengalokasikan Barang
                  4. Exit Program
                  ''')
            pilihan = input("Masukkan angka Menu yang ingin dijalankan: ")
            
            if pilihan == "1":  # Menampilkan Daftar Barang
                daftarBarang(listBarang)
            elif pilihan == "2":  # Mengatur Harga Jual
                hargaBarang(listBarang)
            elif pilihan == "3":  # Mengalokasikan Barang
                alokasiBarang(listBarang)
            elif pilihan == "4":  # Exit Program
                print("Terima kasih telah menggunakan program ini!")
                break
            else:
                print("Pilihan tidak valid! Silakan pilih menu 1-4.")
    else:
        print("Username/password yang Anda input salah. Masukkan kembali username dan password yang benar!")
