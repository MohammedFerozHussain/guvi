x = list(input())
sum=""
for i in range(len(x)):
    if x!=x[::-1]:
        break
    x.pop()
for i in range(len(x)):
    sum+=i
print(sum)
