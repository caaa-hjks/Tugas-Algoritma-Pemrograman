jumlah = int(input("Masukkan jumlah bilangan: "))

i = 1
total = 0

while True:
    data = int(input(f"Masukkan data ke-{i}: "))
    total += data
    i += 1

    if i > jumlah:
        break

rata_rata = total / jumlah

print("Nilai rata-rata =", rata_rata)