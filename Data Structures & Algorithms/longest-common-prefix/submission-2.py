class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen=1000000
        for i in strs:
            l=len(i)
            if(l<minlen):
                minlen=l
        print(minlen)
        
        i=0
        while(i<minlen):
            for j in strs:
                if(j[i]!=strs[0][i]):
                    return strs[0][:i]
            i+=1
        return strs[0][:i]
        
            

        