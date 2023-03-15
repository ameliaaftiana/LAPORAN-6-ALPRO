#proses
def kali(n):
    hasil=1
    for i in range (1,n+1):
        hasil=hasil*i
    return hasil

#input
n=int(input("Masukkan nilai n = "))

#proses
for i in range (n,0,-1):
    for j in range (i,0,-1):
        if j==i:
            print (kali(i), end=" ") #output
        print (j, end=" ") #output
    print() #output
        