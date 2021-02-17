import random
l=[]
for i in range(0,10**3+1):
    l.append(random.randrange(0,2))
i=0
maxim=0
while i<len(l):
    ok=0
    while i<len(l) and l[i]==0:
        ok+=1
        i+=1
    if ok>maxim:
        maxim=ok
    i+=1
print(maxim)