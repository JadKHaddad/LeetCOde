from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        m = nums[0]
        stack = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] + stack[i-1] > nums[i]:
                stack.append(nums[i] + stack[i-1])
            else:
                stack.append(nums[i])
            m = max(m, stack[i])
        return m


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(Solution().maxSubArray(nums))
