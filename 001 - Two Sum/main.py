from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(nums.__len__()):
            if (sum := target - nums[i]) in nums[i + 1 :]:
                return [i, nums.index(sum, i + 1)]


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum(nums=[3, 3], target=6))
