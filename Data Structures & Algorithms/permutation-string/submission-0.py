class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window={}
        wind2={}
        for i in s1:
            if(i  in window):
                window[i]+=1
            else:
                window[i]=1

            
        L=0
        for R in range(len(s2)):
            if s2[R] in wind2:
                wind2[s2[R]] += 1
            else:
                wind2[s2[R]] = 1
            
            
            if R - L + 1 > len(s1):
                wind2[s2[L]] -= 1
                if wind2[s2[L]] == 0:
                    del wind2[s2[L]]

                L += 1
            
   
            
            if(wind2==window):
                return True
        return False
    
        
            

        