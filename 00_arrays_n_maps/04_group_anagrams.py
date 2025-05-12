# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    result = dict()

    for word in strs:
        key = tuple(sorted(word))
        result[key].append(word)

    final_result = []

    for value in result.values():

        final_result.append(value)
        print(value)

    return final_result

# cheated the part on how to save the key, as was getting error and rest was simple
