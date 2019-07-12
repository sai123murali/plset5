inp=int(input())
li=list(map(int,input().split()[:inp]))
nli=[]
co=0
for i in li:
    if(li.count(i)>1):
        if i not in nli:
             nli.append(i)
if(len(nli)==0):
    print("unique")
print(*nli)
        
        
            