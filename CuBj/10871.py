a, b = input().split()
L = list(map(int, input().split()))
r_L = []
for i in range(int(a)):
    if L[i] < int(b) :
        r_L.append(L[i])
print(' '.join(map(str, r_L)))