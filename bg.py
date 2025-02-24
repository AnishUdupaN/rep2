bglist=[]
n=2
#int(input())
for i in range(n):
    llen=int(input())
    bglist.append([list(map(int,input().split()[:llen])),list(map(int,input().split()[:llen]))])

print(bglist[0])
print(bglist[1])
print(bglist)