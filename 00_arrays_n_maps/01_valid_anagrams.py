# https://leetcode.com/problems/valid-anagram/description/

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# googled built in python function name for sort()
