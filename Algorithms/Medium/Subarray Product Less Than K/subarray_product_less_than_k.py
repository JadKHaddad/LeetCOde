from typing import List


class Solution:  # slow
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        arr = []

        def c(index, sub_arr, prod):
            if nums[index] * prod >= k:
                return False
            sub_arr = sub_arr + [nums[index]]
            arr.append(sub_arr)
            if index == len(nums) - 1:
                return False
            for i in range(index + 1, len(nums)):
                if not c(i, sub_arr, nums[index] * prod):
                    return False
            return True

        for i in range(0, len(nums)):
            c(i, [], 1)

        print(arr)

        return len(arr)


class Solution:  # slow
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = [0]

        def c(index, prod):
            if nums[index] * prod >= k:
                return False

            res[0] += 1

            if index == len(nums) - 1:
                return False

            for i in range(index + 1, len(nums)):
                if not c(i, nums[index] * prod):
                    return False
            return True

        for i in range(0, len(nums)):
            c(i,  1)

        return res[0]


class Solution:  # memory
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        stack = [[]]
        res = 0

        if nums[0] < k:
            stack[0].append(nums[0])
            res = 1

        for i in range(1, len(nums)):
            stack.append([])
            if nums[i] >= k:
                continue

            if nums[i] == 1:
                res += len(stack[i-1]) + 1
                stack[i] = [1] + stack[i-1]
                continue

            stack[i].append(nums[i])
            res += 1

            for val in stack[i-1]:
                if nums[i] * val >= k:
                    break
                stack[i].append(nums[i] * val)
                res += 1

        return res


class Solution:  # good enough
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def c(length):
            return int(length * (length + 1) / 2)

        current_index = 0
        start_index = 0
        fail_index = 0
        prod = 1
        res = 0
        stack_index = 0
        while current_index < len(nums):
            add = False
            to_add = (0, 0)
            for i in range(start_index, len(nums)):
                fail_index = i
                if nums[i] * prod >= k:
                    if nums[i] >= k:
                        current_index = fail_index
                        fail_index = fail_index + 1
                        prod = 1
                        break
                    prod = prod / nums[current_index]
                    break
                prod = nums[i] * prod
                add = True
                to_add = (current_index, i)
            current_index = current_index + 1
            start_index = fail_index
            if add:
                if stack_index == 0:
                    last_end = to_add[1]
                    res = res + c(last_end + 1 - to_add[0])
                    stack_index += 1
                    continue
                if to_add[0] <= last_end:
                    res = res + c(to_add[1] + 1 - to_add[0]) - \
                        c(last_end + 1 - to_add[0])
                    last_end = to_add[1]
                    stack_index += 1
                    continue
                res = res + c(to_add[1] + 1 - to_add[0])
                last_end = to_add[1]
                stack_index += 1

        return res


nums = [10, 5, 2, 6]
k = 100

print(Solution().numSubarrayProductLessThanK(nums, k))
