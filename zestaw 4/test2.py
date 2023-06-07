t = [[2,22,1,7],
    [585,35,438,31],
    [9,8,7,88],
    [5,15,8,8]] 
suma=0
i=0

try:
    print(t[5][5])
    print("tak")
        
except:
    pass

for i,j in enumerate(t):
    print(i,j)

tab=[[i for j in range(10)] for i in range(10)]
for i in tab:
    print(i)