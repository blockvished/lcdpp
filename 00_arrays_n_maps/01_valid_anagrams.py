# https://leetcode.com/problems/valid-anagram/description/

def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# googled built in python function name for sort()

print(isAnagram("llo","ool"))
print(isAnagram("llo","lol"))
