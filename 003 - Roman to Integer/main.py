class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        sum = 0
        for i in d:
            sum += s.count(i) * d[i]
            s = s.replace(i, "")
            if s == "":
                return sum
        return sum


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
