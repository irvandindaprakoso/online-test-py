N=int(input())
S=input()
k=[]
H=S.count('h')/2
k.append(H)
A=S.count('a')/2
k.append(A)
C=S.count('c')
k.append(C)
K=S.count('k')
k.append(K)
E=S.count('e')/2
k.append(E)
R=S.count('r')/2
k.append(R)
T=S.count('t')
k.append(T)
print(int(min(k)), min(k))
