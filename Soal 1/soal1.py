teks1 = open("text1.txt")
teks2 = open("text2.txt")
count = 0

baris1 = teks1.readline()
baris2 = teks2.readline()

while baris1 or baris2:
    count += 1
    if baris1 != baris2:
        print(f"Ditemukan perbedaan pada baris ke-{count} !")
        print(f"Teks 1 : {baris1.strip()}")
        print(f"Teks 2 : {baris2.strip()}")
        print("")
    baris1 = teks1.readline()
    baris2 = teks2.readline()

teks1.close()
teks2.close()