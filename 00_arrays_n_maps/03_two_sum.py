# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    uniques = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        if difference in uniques:
            print([uniques[difference], i])
            return [uniques[difference], i]
        uniques[nums[i]] = i


# well cheated in unpotimised as well
# optimised but after a week did optimised ver.
# can use for i, num in enumerate(nums): instead

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))

    # for i, num in enumerate(nums):
    #     difference = target - num
    #     if difference in uniques:
    #         return [uniques[difference], i]
    #     uniques[num] = i
