class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxc=0
        c=0
        charset=set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
                c-=1
            charset.add(s[r])
            c+=1
            maxc=max(c,maxc)
        return maxc
            
        

        