from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        jumps = 0
        index = 0
        if index >= l - 1:
            return jumps
        while True:
            max = -1
            new_index = 0
            for i in range(index + 1, index + nums[index] + 1):
                if i >= l - 1:
                    return jumps + 1
                distance = i - index
                if distance + nums[i] >= max:
                    max = distance + nums[i]
                    new_index = i
            index = new_index
            jumps += 1


nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
print(Solution().jump(nums))
