a=int(input())
li=list(map(int,input().split()[:a]))
co=0
nli=[]
for i in range(len(li)):
    if(li.count(i)==1):
        nli.append(i)
print(*nli)
    