class Solution:

    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        s = s.lower()

        while a < b:
            if not s[a].isalnum():
                a += 1
                continue

            if not s[b].isalnum():
                b -= 1
                continue

            if s[a] != s[b]:
                return False

            a += 1
            b -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True

        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if self.isPalindrome(temp):
                return True

        return False