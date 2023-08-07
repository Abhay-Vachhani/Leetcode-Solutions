class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        n = x
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        return rev == x


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
