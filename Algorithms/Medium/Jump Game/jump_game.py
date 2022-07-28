from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        for i in range(0, len(nums)):
            if nums[i] != 0:
                continue
            succ = False
            # nums[i] is a zero, see if a cell can jump over i or can reach the end
            for j in range(0, i):
                index = i-j-1
                num = nums[index]
                distance = i - index
                if num > distance:
                    succ = True
                    break
                if num + index >= len(nums) - 1:
                    return True
            if not succ:
                return False
        return True


nums = [3, 2, 1, 0, 4]

print(Solution().canJump(nums))
