n = int(input()) #n개의 저울추
a = 1 #최종결론
for i in sorted(list(map(int, input().split()))):
    if i>a:
        break
    a+=i
print(a)
