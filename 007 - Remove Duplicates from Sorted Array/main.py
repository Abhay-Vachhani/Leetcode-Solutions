from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = list(set(nums))
        nums[: len(unique)] = sorted(unique)
        return len(unique)


print(Solution().removeDuplicates(nums=[1, 1, 2]))
print(Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
