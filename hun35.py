#a
n=input()
q=len(n)
u=int(q/2)
a=n[0:u]
b=n[u+1:q]
if a==b:
    print("YES")
else:
    print("NO")
