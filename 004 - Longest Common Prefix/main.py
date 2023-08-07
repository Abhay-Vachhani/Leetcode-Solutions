from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for s in strs[0]:
            ans = ans + s
            for i in strs[1:]:
                if not i.startswith(ans):
                    return ans[:-1]
        return ans


print(Solution().longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(strs=["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(strs=[""]))
print(Solution().longestCommonPrefix(strs=["dog", "dog"]))
