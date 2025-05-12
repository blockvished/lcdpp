# https://leetcode.com/problems/valid-anagram/description/

def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# googled built in python function name for sort()

print(isAnagram("llo","ool"))
print(isAnagram("llo","lol"))


# alt method, copy pasted and unsolved
def isAnagramAlt(s: str, t: str)-> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
