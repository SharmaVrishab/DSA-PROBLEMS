# https://www.youtube.com/watch?v=eDmxPfVa81k
from collections import defaultdict
def groupAnagrams(strs):
    anagram_dict = defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c) - ord('a')] +=1
        key = tuple(count)
        # print(count)
        anagram_dict[key].append(s)
    print(anagram_dict)
strs = ["act","pots","tops","cat","stop","hat"]
groupAnagrams(strs)
