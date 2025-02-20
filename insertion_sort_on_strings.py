string=input("Enter the string:")
def insertion_sort_string(s):
    chars=list(s)
    for i in range(1, len(chars)):
        key=chars[i]
        j=i-1
        while j>=0 and key<chars[j]:
            chars[j+1]=chars[j]
            j-=1
        chars[j+1]=key
    return ''.join(chars)
sorted_string=insertion_sort_string(string)
print("Sorted string:",sorted_string)
