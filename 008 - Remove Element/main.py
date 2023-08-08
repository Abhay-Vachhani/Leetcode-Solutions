from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = [i for i in nums if i != val]
        nums[: (l := len(removed))] = removed
        return l


print(Solution().removeElement(nums=[3, 2, 2, 3], val=3))
