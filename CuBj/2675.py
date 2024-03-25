t = int(input())
for i in range(t):
    a, b = input().split()
    for j in b:
        print(j*int(a), end = "")
    print()