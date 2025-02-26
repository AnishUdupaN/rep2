def binary_search(array,search_element):
    high=len(array)-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if array[mid]==search_element:
            return mid
        elif search_element<array[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

array=[1,2,3,4,5,6,7,8,9,10]
search_element=7
index=binary_search(array,search_element)
print(f"Element {search_element} found at index {index}")
