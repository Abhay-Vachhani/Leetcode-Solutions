from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = []
        digits[-1] += 1
        c = 0
        for i in digits[::-1]:
            i += c
            c = i - 9
            if c < 0:
                c = 0
            if i > 9:
                nums.append(0)
            else:
                nums.append(i)
        if c > 0:
            nums.append(c)
        return nums[::-1]


print(Solution().plusOne(digits=[1, 2, 3]))
print(Solution().plusOne(digits=[4, 3, 2, 1]))
print(Solution().plusOne(digits=[9]))
print(Solution().plusOne(digits=[8, 9, 9, 9]))
