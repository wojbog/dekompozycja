tab=[[2,4,-4],[1,-4,3],[-6,-9,5]]

def lu(A):
    n=len(A)
    L=[]
    U=[]
    z=0
    while(z<n):
        q=0
        g=[]
        h=[]
        while(q<n):
            if(z>q):
                g.append(-1)
                h.append(0)
            elif(z==q):
                g.append(1)
                h.append(-1)
            else:
                g.append(0)
                h.append(-1)
            q+=1
        L.append(g)
        U.append(h)
        z+=1
    del g
    del h,z,q
    for j in range(n):
        i=0
        while(i<=j):
            suma=0
            k=0
            while(k<=(i-1)):
                suma+=(L[i][k]*U[k][j])
                k+=1
            wynik=A[i][j]-suma
            U[i][j]=wynik
            i+=1
        while(i>j and i<n):
            suma = 0
            k = 0
            while (k <= (j - 1)):
                suma += (L[i][k] * U[k][j])
                k+=1
            wynik = (A[i][j] - suma)/U[j][j]
            L[i][j] = wynik
            i += 1
    return {'L':L,'U':U}


tab=lu(tab)
print('L')
print(tab['L'])
print('U')
print(tab['U'])
