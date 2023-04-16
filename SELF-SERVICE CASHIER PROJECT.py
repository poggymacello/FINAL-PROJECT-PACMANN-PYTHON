import random
import string

import random
import string

class Transaction:
    def __init__(self):
        # Inisialisasi atribut ID transaksi, item yang dipesan, dan total harga transaksi
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.items = {}
        self.total = 0

    def add_item(self, name, qty, price):
        # Menambahkan item ke dalam daftar item yang dipesan
        # Menghitung harga total transaksi berdasarkan item yang ditambahkan
        try:
            qty = int(qty)
            price = int(price)
        except ValueError:
            print("Jumlah barang dan harga barang harus berupa angka")
            return

        if name in self.items:
            self.items[name]['qty'] += qty
        else:
            self.items[name] = {'qty': qty, 'price': price}
        self.total += qty * price

    def update_item_name(self, name, new_name):
        # Mengganti nama item yang dipesan
        if name in self.items:
            self.items[new_name] = self.items.pop(name)

    def update_item_qty(self, name, new_qty):
        # Mengganti jumlah item yang dipesan
        # Menghitung harga total transaksi berdasarkan perubahan jumlah item
        try:
            new_qty = int(new_qty)
        except ValueError:
            print("Jumlah barang harus berupa angka")
            return

        if name in self.items:
            price = self.items[name]['price']
            self.total -= self.items[name]['qty'] * price
            self.items[name]['qty'] = new_qty
            self.total += new_qty * price

    def update_item_price(self, name, new_price):
        # Mengganti harga item yang dipesan
        # Menghitung harga total transaksi berdasarkan perubahan harga item
        try:
            new_price = int(new_price)
        except ValueError:
            print("Harga barang harus berupa angka")
            return

        if name in self.items:
            qty = self.items[name]['qty']
            self.total -= qty * self.items[name]['price']
            self.items[name]['price'] = new_price
            self.total += qty * new_price

    def delete_item(self, name):
        # Menghapus item dari daftar item yang dipesan
        # Menghitung harga total transaksi berdasarkan item yang dihapus
        for item in self.items:
            if item['name'] == name:
                qty = item['qty']
                price = item['price']
                self.items.remove(item)
                self.total -= qty * price
                break

    def reset_transaction(self):
        # Menghapus semua item dan mereset total harga transaksi
        self.items = {}
        self.total = 0

    def check_order(self):
        # Memeriksa apakah item yang dipesan valid
        if len(self.items) == 0:
            print("Belum ada barang yang dipesan.")
            return
        for name, item in self.items.items():
            if item['qty'] <= 0 or item['price'] <= 0:
                print(f"Input salah pada barang '{name}'. Harap cek kembali.")
                return
        print("Pemesanan sudah benar.")

    def total_price(self):
        # Menghitung total harga transaksi setelah diskon
        # Mengembalikan harga total setelah diskon
        total = 0
        for item in self.items:
            total += self.items[item]['qty'] * self.items[item]['price']
        if total > 500000:
            total *= 0.9
        elif total > 300000:
            total *= 0.92
        elif total > 200000:
            total *= 0.95
        return total

    def print_transaction(self):
        print("Item\tJumlah item\tHarga/item\tHarga total")
        for name, info in self.items.items():
            print(f"{name}\t{info['qty']}\t\t{info['price']}\t\t{info['qty']*info['price']}")
    
    def thank_you(self):
        print("Terima kasih sudah berbelanja di PACMANN Mart!")
        print("Semoga Anda puas dengan pelayanan kami.")
        exit()
    
import datetime
def generate_receipt(items, discount_percent):
    try:
        receipt_file = f"receipt-{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.txt"
        with open(receipt_file, "w") as file:
            file.write("Receipt\n")
            file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            if not items:
                file.write("Cart is empty\n")
            else:
                file.write("Items in cart:\n")
                for item in items:
                    item_total = item["price"] * item["qty"]
                    file.write(f"{item['name']} - {item['qty']} x {item['price']} = {item_total}\n")
                discount_amount = (discount_percent / 100) * total_price(items)
                discounted_total = total_price(items) - discount_amount
                file.write("\n")
                file.write(f"Total price: {total_price(items)}\n")
                file.write(f"Discount ({discount_percent}%): -{discount_amount}\n")
                file.write(f"Discounted price: {discounted_total}\n")
        print(f"Receipt generated successfully: {receipt_file}")
    except Exception as e:
        print(f"Failed to generate receipt: {str(e)}")

def total_price(items):
    return sum(item["price"] * item["qty"] for item in items)