class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        for i in range(lh):
            for x in range(ln):
                if (y := i + x) >= lh or haystack[y] != needle[x]:
                    break
            else:
                return i
        return -1


print(Solution().strStr(haystack="sadbutsad", needle="sad"))
print(Solution().strStr(haystack="leetcode", needle="leeto"))
print(Solution().strStr(haystack="aaa", needle="aaaa"))
print(Solution().strStr(haystack="hello", needle="ll"))
