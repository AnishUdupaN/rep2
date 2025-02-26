def custom_range(*args):
    start=0
    step=1
    if len(args)==1:
        stop=args[0]
    elif len(args)==2:
        start,stop=args
    else:
        start,stop,step=args
    if step>0:
        while start<stop:
            yield start
            start+=step
    else:
        while start>stop:
            yield start
            start+=step

for i in custom_range(40,80,4):
    print(i,end='  ')
print()
for i in custom_range(1,10):
    print(i,end='  ')
print()
for i in custom_range(10):
    print(i,end='  ')
print()
for i in custom_range(0,10,2):
    print(i,end='  ')
print()
for i in custom_range(10,0,-2):
    print(i,end='  ')
print()
