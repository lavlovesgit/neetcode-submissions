class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=""
        for i in strs:
            encode=encode+str(len(i))+"#"+i
        print(encode)
        return encode





    def decode(self, s: str) -> List[str]:
        i=0
        out=[]
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j+=1
            l = int(s[i:j])
            out.append(s[j+1:j+l+1])
            i=j+l+1

        return out
            
            

