#input
tinggi=int(input("Masukkan tinggi = "))
lebar=int(input("Masukkan lebar = "))

angka=1

#proses
for i in range (0, tinggi):
    for j in range (0, lebar):
        print (angka, end=" ") #output
        angka=angka+1
    print() #output
    lebar=lebar
        


