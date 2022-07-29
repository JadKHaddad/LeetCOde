from typing import List

# slow
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) < 3 or k < 2:
            return sum(nums)
        for i in range(1, len(nums)):
            index = len(nums) - 1 - i
            next = nums[index + 1:min(len(nums), index + k + 1)]
            nums[index] = nums[index] + max(next)
        return nums[0]

# alot of memory
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) < 1:
            return 0
        seen = {}
        def m(index: int, nums: List[int]):
            if len(nums) == 1:
                return nums[0]
            if index in seen:
                return seen[index]
            for i in range(1, min(len(nums), k + 1)):
                if nums[i] > 0:
                    return nums[0] + m(index + i, nums[i:])
            seen[index] = nums[0] + max([m(index + i, nums[i:]) for i in range(1, min(len(nums), k + 1))])
            return seen[index] 
        return m(0, nums)

# dp, internet
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = [0]
        i = 1
        n = len(nums)
        while i < n:
            if (q[0] + k) < i:
                q.pop(0)
            nums[i] += nums[q[0]]
            while len(q) > 0 and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            i += 1
        return nums.pop()

nums = [10, -5, -2, 4, 0, 3]
k = 3

print(Solution().maxResult(nums, k))