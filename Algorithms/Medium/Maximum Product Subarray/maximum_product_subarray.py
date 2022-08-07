from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        m = nums[0]
        stack = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            m_m = [nums[i], nums[i]]
            for j in range(0, 2):
                if nums[i] * stack[i-1][j] > m_m[0]:
                    m_m[0] = (nums[i] * stack[i-1][j])
                if nums[i] * stack[i-1][j] < m_m[1]:
                    m_m[1] = (nums[i] * stack[i-1][j])
            m = max(m, m_m[0])
            stack.append(m_m)
        return m


nums = [2, 3, -2, 4]


print(Solution().maxProduct(nums))
