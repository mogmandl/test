a = int(input())
result = 1

for i in range(a):
    H, W, N = map(int, input().split())
    H_f = result * (100 * H) + (W)
    print(H_f)