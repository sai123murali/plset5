a=int(input())
li=list(map(int,input().split()[:a]))
b=False
for i in li:
    if(li.count(i)>1):
        b=True
        break
if b:
    print(i)
else:
    print("unique")
  