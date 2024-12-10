def bruteforce_method(arr,t):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i]+arr[j] == t:
                return [i,j]
    return []


def hashmap_onepass(arr,t):
    prevMap = {}
    for i,n  in enumerate(arr):
        diff = t - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
        
nums = [3,4,5,6]
target = 7
print(bruteforce_method(nums,target))
print(hashmap_onepass(nums,target))