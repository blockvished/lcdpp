# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        result[key].append(word)

    final_result = []

    for value in result.values():

        final_result.append(value)
        # print(value)

    return final_result

# cheated the part on how to save the key, as was getting error and rest was simple

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["A"]))
print(groupAnagrams([""]))
