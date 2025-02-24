num_of_iterations=1
#int(input())
boys_list=[]
girls_list=[]
full_list=[]
flag=False

for i in range(num_of_iterations):
    n=int(int(input()))
    boys_list=list(map(int,input().split()[:n]))
    girls_list=list(map(int,input().split()[:n]))
    
boys_list.sort()
girls_list.sort()
print(boys_list)
print(girls_list)




if boys_list[0]<girls_list[0]:
    for i in range(len(boys_list)):
        full_list.append(boys_list[i])
        full_list.append(girls_list[i])
elif boys_list[0]>=girls_list[0]:
    for i in range(len(boys_list)):
        full_list.append(girls_list[i])
        full_list.append(boys_list[i])


for i in range(1,len(full_list)):
    if full_list[i]>=full_list[i-1]:
        flag=True
    else:
        flag=False
if flag:
    print('YES')
else:
    print("NO")









[5, 6, 8, 9]
[0, 3, 5, 7]
[0, 5, 3, 6, 7, 9]