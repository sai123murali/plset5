inp=int(input())
li=list(map(int,input().split()[:inp]))
li.sort(reverse=True)
#print(li)

if li[0]==0:
    print("0")
else:
    for i in range(inp):
         print(li[i],end="")