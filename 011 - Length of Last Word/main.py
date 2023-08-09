class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        isSpace = False
        for i in range(len(s)):
            if isSpace and s[i] != " ":
                cnt = 0
                isSpace = False
            if s[i] != " ":
                cnt += 1
            else:
                isSpace = True
        return cnt


print(Solution().lengthOfLastWord(s="Hello World"))
print(Solution().lengthOfLastWord(s="   fly me   to   the moon  "))
print(Solution().lengthOfLastWord(s="luffy is still joyboy"))
print(Solution().lengthOfLastWord(s="a"))
print(Solution().lengthOfLastWord(s="abc"))
print(Solution().lengthOfLastWord(s="a "))
