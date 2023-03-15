#input
n=int(input("Masukkan n = "))

#proses
prima=[]
for i in range (0,n):
    if (i==2 or i==3 or i==7) or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
        prima.append(i)

#output
print ("Bilangan prima terdekat adalah", prima[-1])
