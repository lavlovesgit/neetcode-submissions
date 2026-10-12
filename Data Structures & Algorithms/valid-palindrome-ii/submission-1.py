def isPalindrome(s: str) -> bool:
        l=0
        r=len(s)-1
        s=s.lower()
        while(l<r):
            
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
class Solution:
    
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if not isPalindrome(s[:i]+s[i+1:]):
                continue
            else:
                return True
        return False
                

        