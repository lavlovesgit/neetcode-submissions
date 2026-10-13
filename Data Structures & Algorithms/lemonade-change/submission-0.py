class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change={5:0,10:0,20:0}
        for i in bills:
            change[i]=change[i]+1
            if i==10:
                if change[5]<1:
                    return False
                change[5]-=1
            if i==20:
                if change[5]>=1 and change[10]>=1:
                    change[5]-=1
                    change[10]-=1
                elif change[5]>=3:
                    change[5]-=3

                else:
                    return False
                 

                
        return True
                
        