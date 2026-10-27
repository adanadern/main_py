# variabel data dan tipe data
nmmhs = input("Masukan Nama :")
nalgo =int(input("Masukan Nilai Algoritma :"))
nbasisdata =int(input("masukan Nilai Basis Data :"))
npancasila =int(input("masukan Nilai Pancasila :"))
nagama =int(input("masukan Nilai Agama :"))
nfisika =int(input("Masukan Nilai Fisika :"))
nbahasainggris =int(input("Masukan Nilai Bahasa Inggris :"))
rata_rata = (nalgo + nbasisdata + npancasila + nagama + nfisika + nbahasainggris) / 7
print(rata_rata)

# penentuan lulus atau tidak
if rata_rata >=80 and rata_rata <=100:
    print("Nilai : A")
elif rata_rata >=70 and rata_rata <=80:
    print("Nilai : B")
elif rata_rata >=55 and rata_rata <=70:
    print("Nilai : C")
elif rata_rata >=35 and rata_rata <=55:
    print("Nilai : D")
elif rata_rata >=15 and rata_rata <=35:
    print("Nilai : E")
    
else:
    # cukup menampilkan hasil
    # maka
    print("Nilai lebih dari 100 atau dibawah 50")
    