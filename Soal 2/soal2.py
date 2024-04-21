file = input("Nama File : ")
handle = open(file)

for baris in handle:
    baris = baris.split("||")

    print(baris[0])
    jawaban = input("Jawab : ").lower()
    if jawaban == baris[1].strip().lower():
        print("Jawaban benar!")
    else:
        print("Jawaban salah!")

handle.close()