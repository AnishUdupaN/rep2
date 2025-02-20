numsum=0
num=list(map(int,input('Enter a Number: ').split()))
#num=list(input('Enter a Number: ').split())
for i in range(len(num)):
    if i%2==0 and num[i]%2==0:
        numsum+=num[i]
        print(numsum,end='  ')

print()
#print(numsum)
