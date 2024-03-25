# a, b = map(int, input().split())
# minute = b - 45
# hour = a - 1

# if hour < 0 :
#     print(23, 60 + minute)
# elif minute < 0 :
#     print(a - 1, 60 + minute)
# else :
#     print(a, minute)

H, M = map(int, input().split())

if M < 45 :
    if H == 0:
        H = 23
        M += 60
    else :
        H -= 1
        M += 60

print(H, M - 45)