#for single integer input only(for digits within an integer)
nums=list(int(x) for x in list(input("Enter a number: ")))
numlist=[]
for i in range(len(nums)):
    if i%2==0 and nums[i]%2==0:
        numlist.append(nums[i])
print(numlist)
print(sum(numlist))

