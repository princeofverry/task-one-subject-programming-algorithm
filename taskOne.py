import math

# nomor satu
print("\n")
print("perhitungan luas persegi panjang")
print("\n")

p = int(input("masukkan panjang= "))
l = int(input("masukkan lebar= "))


def luasPersegiPanjang(p,l):
    luas = p*l
    if luas < 0:
        print("masukkan angka lebih dari 0")
    else:
        print("luas = " + str(luas))



luasPersegiPanjang(p,l)
print("\n")


#nomor dua
print("perhitungan luas lingkaran")
print("\n")

r = int(input("masukkan jari-jari= "))

def lingkaran(r):
    luas = math.pi*r**2
    if luas < 0:
        print("masukkan angka lebih dari 0")
    else:
        print("luas lingkaran = " + str(luas))

lingkaran(r)
print("\n")



#nomor tiga
#masukkan nomor m-n
print("bilangan fibonacci")

m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

# Masukkan angka fibonacci awal (nilai awal)
fib_1 = 0
fib_2 = 1

# pengecekan deret fibonnaci

if m > n:
    print("angka yang seharusnya adalah m < n")

# Periksa apakah m > 1, jika ya, hitung deret Fibonacci hingga m
if m > 1:
    for i in range(2, m):
        fib = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib

# Hitung dan cetak deret Fibonacci dari m hingga n
fib_list = []
for i in range(m, n+1):
    if i == 0:
        fib_list.append(0)
    elif i == 1:
        fib_list.append(1)
    else:
        fib = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib
        fib_list.append(fib)
print("berikut adalah deret fibonacci dari S" + str(m) + " sampai S" + str(n))
print(*fib_list, sep=", ")
