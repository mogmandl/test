a, b = map(int, input().split())
c, d = map(int, input().split())
money = int(input())

print("청구서\n"+"="*25+"\n음식\t수량\t가격\n"+f"음식1\t{a}\t{a*b}\n음식2\t{c}\t{c*d}\n합계\t{a+c}\t{a*b+c*d}")
print(a*b+c*d <= money) 