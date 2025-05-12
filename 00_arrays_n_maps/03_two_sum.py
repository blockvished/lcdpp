# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    uniques = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        if difference in uniques:
            return [uniques[difference], i]
        uniques[difference] = i

# well cheated in unpotimised as well
# optimised but after a week did optimised ver.
# can use for i, num in enumerate(nums): instead
