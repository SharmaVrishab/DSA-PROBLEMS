def brute_anagram_test(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
//solution 2    
def anagram_test_hashtable(s,t):
    if len(s) != len(t):
        return False
    # defining hashtable
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1+countS.get(s[i],0)
        countT[t[i]] = 1+countT.get(t[i],0)
    return  countS == countT
    

s = "racecar"
t = "carrace"
print(brute_anagram_test(s,t))
print(anagram_test_hashtable(s,t))

