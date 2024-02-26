#cek apakah sebuah bilangan prima
def is_prima(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# cetak sebuah bilangan prima dari 1 sampai 100
print("bilangan prima antara 1 dan 100")  
for i in range(2, 101):
    if is_prima(i):
        print(i)       