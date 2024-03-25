a = input().upper()
S_a = list(set(a))
L_a = []

for i in S_a :
    L_a.append(a.count(i))

if L_a.count(max(L_a)) > 1 :
    print("?")
else :
    print(S_a[L_a.index(max(L_a))])