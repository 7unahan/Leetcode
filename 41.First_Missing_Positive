class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [*set(nums)]
        nums.sort()
        if nums[len(nums)-1]<1:
            return 1
        nums = [item for item in nums if item > 0]
        if nums[0] == 1:
            if nums[(len(nums)-1)] == len(nums):
                return nums[(len(nums)-1)]+1
            else:
                for i in range(len(nums)-1):
                    if (nums[i+1] - nums[i]) != 1:
                        return nums[i]+1
        return 1 
