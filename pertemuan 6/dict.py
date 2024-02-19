belanja = [
    {"buah ":"semangka", "harga": 12000},
    {"buah ":"nanas", "harga": 10000},
    {"buah ":"pepaya", "harga": 15000},
    ]

total_belanja = 0
for item in belanja:
    total_belanja += item["harga"]

print("total belanja : ", total_belanja)