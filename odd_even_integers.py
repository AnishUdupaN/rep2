nums=list(map(int,input("Enter the numbers: ").split()))
#nums=[int(i) for i in input("Enter the numbers: ").split()]
numlist=[]
for i in range(len(nums)):
    if i%2==0 and nums[i]%2==0:
        numlist.append(nums[i])
print(numlist)
print(sum(numlist))