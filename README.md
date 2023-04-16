# PROYEK-PACMANN
SELF-SERVICE SUPERMARKET CASHIER

DOKUMENTASI :

1. LATAR BELAKANG
Andi memiliki supermarket yang ingin membuat sistem kasir self-service agar pelanggan dapat memasukkan barang yang ingin dibeli dengan sendiri, tanpa harus dilakukan oleh kasir. Sistem ini harus dapat menghitung harga dan menampilkan total harga yang harus dibayar oleh pelanggan. Tujuan dari pembuatan sistem ini adalah untuk meningkatkan efisiensi proses bisnis dan memberikan kemudahan bagi pelanggan dalam berbelanja.

2. PENJELASAN REQUIREMENTS OBJECTIVES
Untuk membuat program sistem kasir self-service, beberapa requirements atau tujuan yang perlu dipenuhi antara lain:
 a. Pelanggan dapat memasukkan item yang ingin dibeli, jumlah item, dan harga item.
 b. Sistem dapat menghitung total harga yang harus dibayar oleh pelanggan.
 c. Sistem dapat menampilkan total harga yang harus dibayar.
 d. Program harus bersifat modular, menggunakan clean code (PEP8), dan memiliki exception handling untuk mengatasi kesalahan.

3. PENJELASAN ALUR CODE/FLOWCHART
Berikut adalah alur code atau flowchart dari program sistem kasir self-service:
 a. Program akan meminta input dari pengguna mengenai item yang akan dibeli. Input yang diminta meliputi nama item, harga, dan jumlah item yang akan dibeli. Input tersebut akan diproses menggunakan method add_item dari class Transaction, yang akan menambahkan item dan jumlahnya ke dalam cart.
 b. Setiap kali pengguna menambahkan item baru ke dalam cart, program akan menampilkan kembali daftar item yang ada di cart, total harga, serta pilihan untuk melanjutkan membeli atau untuk checkout.
 c. Jika pengguna memilih untuk melanjutkan membeli, program akan kembali ke tahap ke-3 dan mengulangi proses.
 d. Jika pengguna memilih untuk checkout, program akan menghitung total harga dari semua item di cart menggunakan method total_price dan menampilkan total harga tersebut.
 e. Setelah pengguna memasukkan persentase diskon (atau tidak memasukkan apa-apa), program akan menampilkan total harga setelah diskon dan meminta pengguna untuk membayar. 
 f. Akhirnya, program akan mencetak receipt dengan memanggil method generate_receipt dari class Transaction, yang akan menampilkan detail pembelian dan harga di sebuah file teks.

4. PENJELASAN ATTRIBUTES & FUNCTION 
Pada kode yang diberikan, terdapat class Transaction yang memiliki beberapa function atau method dan attribute. Berikut adalah penjelasan dari function/attribute tersebut:

Attribute:
items: list yang berisi dictionary dari item yang dibeli oleh customer.

Functions:
add_item(): method untuk menambahkan item ke dalam cart.
remove_item(): method untuk menghapus item dari cart.
total_price(): method untuk menghitung total harga dari semua item yang dibeli oleh customer.
generate_receipt(): method untuk meng-generate receipt berisi detail belanjaan customer.
display_items(): method untuk menampilkan daftar item yang ada di dalam cart.

5. DEMONSTRASI TEST CASE DAN OUTPUT
Berikut adalah dua contoh test case beserta outputnya:

  a. TEST CASE 1
## Membuat objek transaksi baru
transaction = Transaction()

## Menambahkan beberapa item ke dalam transaksi
transaction.add_item("Barang A", 2, 10000)
transaction.add_item("Barang B", 3, 5000)

## Memperbarui jumlah barang untuk "Barang A"
transaction.update_item_qty("Barang A", 3)

## Memperbarui harga barang untuk "Barang B"
transaction.update_item_price("Barang B", 6000)

## Menghapus "Barang B" dari transaksi
transaction.delete_item("Barang B")

## Mengecek transaksi
transaction.check_order()

## Mencetak transaksi
transaction.print_transaction()

## Menghitung total harga dan memberikan diskon jika berlaku
total = transaction.total_price()

## Menghasilkan struk belanja
generate_receipt(transaction.items, 10)

OUTPUT
Pemesanan sudah benar.
Item    Jumlah item     Harga/item      Harga total
Barang A        3               10000           30000

Receipt generated successfully: receipt-2023-04-16 12-39-22.txt

 b. TEST CASE 2
## Membuat objek transaksi baru
t = Transaction()

## Menambahkan beberapa item ke dalam transaksi
t.add_item("Baju", 2, 100000)
t.add_item("Celana", 1, 150000)
t.add_item("Sepatu", 1, 300000)

## Mencetak transaksi
print("Transaksi awal:")
t.print_transaction()

## Mengupdate nama item
t.update_item_name("Baju", "Kemeja")

## Mengupdate jumlah item
t.update_item_qty("Celana", 2)

## Mengupdate harga item
t.update_item_price("Sepatu", 280000)

## Menghapus Item
t.delete_item("Baju")

## Mencetak Transaksi Baru
print("\nTransaksi setelah perubahan:")
t.print_transaction()

## Memeriksa Pesanan
t.check_order()

## Menghitung total harga dan memberikan diskon jika berlaku
total = t.total_price()

## Mencetak total harga
print(f"\nTotal harga: {total}")

## Menghasilkan struk belanja
generate_receipt(t.items, 10)

OUTPUT :

Transaksi awal:
Item    Jumlah item    Harga/item    Harga total
Baju    2              100000        200000
Celana  1              150000        150000
Sepatu  1              300000        300000

Transaksi setelah perubahan:
Item    Jumlah item    Harga/item    Harga total
Kemeja  2              100000        200000
Celana  2              150000        300000
Sepatu  1              280000        280000

Pemesanan sudah benar.

Total harga: 604000.0

Receipt generated successfully: receipt-2023-04-16 13-08-56.txt
