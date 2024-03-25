a = int(input())
b = int(input())
c = int(input())

result = a * b * c
strR = str(result)

for i in range(10) :
    print(strR.count(str(i)))
