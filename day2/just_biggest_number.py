def find_next_bigger_number(n):
    num_str=list(str(n))
    i=len(num_str)-2
    while i>=0 and num_str[i]>=num_str[i+1]:
        i-=1
    if i==-1:
        return n
    j=len(num_str)-1
    while num_str[j]<=num_str[i]:
        j-=1
    num_str[i],num_str[j]=num_str[j],num_str[i]
    num_str[i+1:]=reversed(num_str[i+1:])
    return int(''.join(num_str))

number=int(input("Enter a number : "))
next_bigger_number=find_next_bigger_number(number)
print(f"The number just bigger than {number} is {next_bigger_number}")
