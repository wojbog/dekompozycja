tab=[[4,2,2],[2,5,3],[2,3,6]]

def cho(A):
    import math
    n=len(A)
    L=[]
    z=0
    while(z<n):
        q=0
        g=[]
        while(q<n):
            if(z>=q):
                g.append(-1)
            else:
                g.append(0)
            q+=1
        L.append(g)
        z+=1
    del g,z,q
    for i in range(n):
        j = i
        k = 0
        suma = 0
        while (k <= (i - 1)):
            suma += (L[i][k] * L[i][k])
            k += 1
        L[i][j] = math.sqrt(A[i][j] - suma)
        while (j < n):
            suma = 0
            k = 0
            while (k <= (i - 1)):
                suma += (L[j][k] * L[i][k])
                k += 1
            wynik = (A[j][i] - suma) / L[i][i]
            L[j][i] = wynik
            j += 1
    LT=[]

    for i in range(n):
        g = []
        for j in range(n):
            g.append(L[j][i])
        LT.append(g)

    return {'L':L,'LT':LT}

wy=cho(tab)
print("L:")
print(wy['L'])
print("L*")
print(wy['LT'])