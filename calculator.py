# cuman buat latihan

border = "=" * 40
line = "-" * 40

print(border)
print("\nCalculator 2.0\n")
print("\t(1)Penjumlahan")
print("\t(2)Pengurangan")
print("\t(3)Perkalian")
print("\t(4)Pembagian")
print("\t(5)Persegi")
print("\t(6)Persegi Panjang")

path = input("\n\t\tMasukkan Angka:")

if path == "1":
    print(line)
    print("\nPertambahan = a + b = c\n")
    a = int(input("\ta = "))
    b = int(input("\tb = "))
    c = a + b
    print(f"\tc = {c}")

if path == "2":
    print(line)
    print("\nPengurangan = a - b = c\n")
    a = int(input("\ta = "))
    b = int(input("\tb = "))
    c = a - b
    print(f"\tc = {c}")

if path == "3":
    print(line)
    print("\nPerkalian = a x b = c\n")
    a = int(input("\ta = "))
    b = int(input("\tb = "))
    c = a * b
    print(f"\tc = {c}")

if path == "4":
    print(line)
    print("\nPembagian = a : b = c\n")
    a = int(input("\ta = "))
    b = int(input("\tb = "))
    c = a / b
    print(f"\tc = {c}")

if path == "5":
    print(line)
    print("\nPersegi\n")
    print("\t(1)Luas")
    print("\t(2)keliling")
    option = input("\t\tMasukkan Angka: ")

    if option == "1":
        print("\nKeliling = 4 x sisi = c")

        sisi = int(input("\tsisi = "))

        keliling = sisi * 4
        print(f"keliling = {keliling}")
    if option == "2":
        print("\nLuas = sisi x sisi = c")

        sisi = int(input("\tsisi = "))

        luas = sisi * sisi
        print(f"Luas = {luas}")
if path == "6":
    print(line)
    print("\nPersegi Panjang\n")
    print("\t(1)Luas")
    print("\t(2)keliling")
    option = input("\t\tMasukkan Angka: ")

    if option == "1":
        print("\nKeliling = 4 x sisi = c")

        sisi = int(input("\tsisi = "))

        keliling = sisi * 4
        print(f"keliling = {keliling}")
    if option == "2":
        print("\nLuas = sisi x sisi = c")

        sisi = int(input("\tsisi = "))

        luas = sisi * sisi
        print(f"Luas = {luas}")

print("\n")
print(border)
