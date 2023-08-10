class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = (a, b) if len(a) > len(b) else (b, a)

        la, lb = len(a) * -1, len(b) * -1

        c = 0
        s = ""

        for i in range(-1, la - 1, -1):
            x = 0
            if i >= la:
                x += int(a[i])

            if i >= lb:
                x += int(b[i])
            x += c
            if x == 1:
                s += "1"
                x -= 1
            elif x == 0:
                if s == "":
                    s = "0"
                else:
                    s += "0"
            elif x == 2:
                s += "0"
                x -= 1
            elif x == 3:
                s += "1"
                x -= 2

            c = x

        if c == 1:
            s += "1"
        elif s == 0:
            if s == "":
                s = "0"
            else:
                s += "0"
        elif c == 2:
            s += "0"
        elif c == 3:
            s += "1"
        return s[::-1]


print(Solution().addBinary(a="11", b="1"))
print(Solution().addBinary(a="1010", b="1011"))
print(Solution().addBinary(a="1", b="111"))
print(Solution().addBinary(a="1111", b="1111"))
print(Solution().addBinary(a="0", b="0"))
