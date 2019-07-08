a=int(input(""))
li=list(map(int,input("").split()[:a]))
sum=0
for i in range(0,a):
    sum=sum+li[i]
print(sum//a)