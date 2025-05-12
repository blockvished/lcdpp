# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums) -> bool:
    unique = set()

    for i in nums:
        if i in unique:
            return True
        unique.add(i)
    return False

print(containsDuplicate([2,3,46,8,6]))
print(containsDuplicate([2,3,46,8,6,6]))

# i used a list first but then used the set as time exceed error on lc
