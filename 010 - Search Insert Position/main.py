from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i + 1


print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))
