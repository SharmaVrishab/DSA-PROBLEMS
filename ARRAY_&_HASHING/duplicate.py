#  check if there are duplicate in the array


#  brute force method
def check_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # Compare with subsequent elements
            if arr[i] == arr[j]:
                return True  # Duplicate found
    return False  # No duplicates
        
def check_duplicate_when_sorted(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False
# we can also store this inside a datastructure that donot store duplicates 
def check_duplicate_when_hashset_is_used(arr):
    seen  = set()
    for i in arr:
        if i  in seen:
            return True
        seen.add(i)
    return False
#  shortest way could be check the length of hashset and array
def shortest_test(arr):
    return  len(set(arr)) < len(arr)
arr = [1,2,3,1]
print(check_duplicate(arr))
print(check_duplicate_when_sorted(arr))
print(check_duplicate_when_hashset_is_used(arr))
print(shortest_test(arr))