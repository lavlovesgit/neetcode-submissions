class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        window=set()
        c=0
        long=0
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
                c -= 1
            window.add(s[R])
            c+=1
            if(c>long):
                long=c
        return long
