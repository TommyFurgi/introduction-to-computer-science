wynik=0
liczba=24
p=0
while liczba>0:
    wynik=(liczba%2) *10**p + wynik
    liczba//=2
    p+=1

print(wynik)

t=[32,24,5324,4324,0,4,22]
for i in range(len(t)):
    for j in range(len(t)-1-i):
        if t[j]>t[j+1]:
            t[j],t[j+1]=t[j+1],t[j]
print(t)

def nwd(a,b):
    while b:
        a,b=b,a%b
    return a
print(nwd(30,60))