from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)
        while True:
            if end - start < 1:
                return [-1, -1]
            mid = int((end - start)/2) + start
            if nums[mid] == target:
                break
            if nums[mid] < target:
                start = mid + 1
                continue
            if nums[mid] > target:
                end = mid
        start = mid
        end = mid
        for i in range(mid, len(nums)):
            if nums[i] > target:
                break
            end = end + 1
        for i in range(mid - 1, -1, -1):
            if nums[i] < target:
                break
            start = start - 1
        return [start, end - 1]


nums = [5, 7, 7, 8, 8, 10]
target = 9

print(Solution().searchRange(nums, target))
