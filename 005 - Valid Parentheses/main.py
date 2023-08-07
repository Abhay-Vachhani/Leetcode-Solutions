class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        openBrackets = d.values()

        for i in s:
            if i in openBrackets:
                st.append(i)
            else:
                if st.__len__() > 0 and st[-1] == d[i]:
                    st.pop()
                else:
                    return False
        return st.__len__() < 1


print(Solution().isValid(s="()"))
print(Solution().isValid(s="()[]{}"))
print(Solution().isValid(s="(]"))
print(Solution().isValid(s="["))
print(Solution().isValid(s="]"))
