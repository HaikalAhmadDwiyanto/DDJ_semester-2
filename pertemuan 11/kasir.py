import tkinter as tk
from tkinter import messagebox

class KasirAplikasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Kasir Toko Central")

        # Inisialisasi daftar barang beserta harganya
        self.daftar_barang = {
            "Kemeja": 150000,
            "Celana": 200000,
            "Jaket": 300000,
            "Dress": 250000,
            "Rok": 180000
        }

        # Dictionary untuk menyimpan status pembelian barang
        self.status_pembelian = {barang: tk.BooleanVar() for barang in self.daftar_barang}

        # Dictionary untuk menyimpan barang yang dipilih beserta jumlahnya
        self.keranjang = {}

        # Label dan input untuk nama pembeli
        self.label_nama_pembeli = tk.Label(root, text="Nama Pembeli:")
        self.label_nama_pembeli.pack()
        self.entry_nama_pembeli = tk.Entry(root)
        self.entry_nama_pembeli.pack()

        # Membuat pilihan barang beserta checkbox
        self.label_barang = tk.Label(root, text="Pilih Barang:")
        self.label_barang.pack()
        for barang in self.daftar_barang:
            checkbox = tk.Checkbutton(root, text=f"{barang} - Rp {self.daftar_barang[barang]:,.0f}",
                                      variable=self.status_pembelian[barang])
            checkbox.pack(anchor="w")

        # Tombol hitung jumlah barang yang dipilih
        self.button_hitung_barang = tk.Button(root, text="Hitung Barang Dipilih", command=self.hitung_barang_dipilih)
        self.button_hitung_barang.pack()

        # Label untuk menampilkan total barang yang dipilih
        self.label_jumlah_barang = tk.Label(root, text="")
        self.label_jumlah_barang.pack()

        # Membuat label dan input untuk jumlah barang
        self.label_jumlah = tk.Label(root, text="Jumlah Barang:")
        self.label_jumlah.pack()
        self.entry_jumlah = tk.Entry(root)
        self.entry_jumlah.pack()

        # Membuat opsi pembayaran
        self.label_bayar = tk.Label(root, text="Pilih Metode Pembayaran:")
        self.label_bayar.pack()
        self.selected_bayar = tk.StringVar(root)
        self.selected_bayar.set("Tunai")  # Default value
        self.option_bayar = tk.OptionMenu(root, self.selected_bayar, "Tunai", "Kartu Kredit", "Transfer Bank")
        self.option_bayar.pack()

        # Tombol hitung total
        self.button_hitung = tk.Button(root, text="Hitung Total", command=self.konfirmasi_pembelian)
        self.button_hitung.pack()

        # Tombol lihat keranjang
        self.button_lihat_keranjang = tk.Button(root, text="Lihat Keranjang", command=self.tampilkan_keranjang)
        self.button_lihat_keranjang.pack()

    def hitung_barang_dipilih(self):
        jumlah_barang = sum(1 for barang in self.daftar_barang if self.status_pembelian[barang].get())
        self.label_jumlah_barang.config(text=f"Total Barang Dipilih: {jumlah_barang}")

    def konfirmasi_pembelian(self):
        nama_pembeli = self.entry_nama_pembeli.get()
        if not nama_pembeli:
            messagebox.showerror("Error", "Nama pembeli belum diisi!")
            return

        total_harga = self.hitung_total()
        if total_harga == 0:
            messagebox.showerror("Error", "Belum ada barang yang dipilih!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin melakukan pembelian dengan total harga Rp {total_harga:,.0f}?")
        if konfirmasi:
            messagebox.showinfo("Pembelian Berhasil", "Pembelian berhasil dilakukan!")
            self.label_total.config(text=f"Total Harga: Rp {total_harga:,.0f}. Metode Pembayaran: {self.selected_bayar.get()}. Pembeli: {nama_pembeli}")
            self.reset_form()

    def reset_form(self):
        # Reset semua input dan status ke nilai awalnya
        self.entry_nama_pembeli.delete(0, tk.END)
        for barang in self.daftar_barang:
            self.status_pembelian[barang].set(False)
        self.entry_jumlah.delete(0, tk.END)
        self.selected_bayar.set("Tunai")
        self.label_total.config(text="")
        self.keranjang.clear()  # Mengosongkan keranjang setelah pembelian selesai

    def tampilkan_keranjang(self):
        if not self.keranjang:
            messagebox.showinfo("Keranjang", "Keranjang masih kosong.")
        else:
            keranjang_text = "Isi Keranjang:\n"
            for barang, jumlah in self.keranjang.items():
                keranjang_text += f"{barang}: {jumlah}\n"
            messagebox.showinfo("Keranjang", keranjang_text)

    def hitung_total(self):
        total_harga = 0
        for barang in self.daftar_barang:
            if self.status_pembelian[barang].get():
                jumlah = int(self.entry_jumlah.get())
                harga_per_barang = self.daftar_barang[barang]
                total_harga += jumlah * harga_per_barang
                # Menambahkan barang ke keranjang
                if barang in self.keranjang:
                    self.keranjang[barang] += jumlah
                else:
                    self.keranjang[barang] = jumlah
        return total_harga

if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = KasirAplikasi(root)
    root.mainloop()