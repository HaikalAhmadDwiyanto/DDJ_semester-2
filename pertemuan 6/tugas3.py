data_penjualan = [
    {"produk ":"baju", "jumlah": 20},
    {"produk":"celana", "jumlah": 15},
    {"produk":"sepatu", "jumlah": 25},
    {"produk":"tas", "jumlah": 10},
    ]

total_penjualan = 0
for item in data_penjualan:
    total_penjualan += item["jumlah"]

print("total penjualan : ", total_penjualan)