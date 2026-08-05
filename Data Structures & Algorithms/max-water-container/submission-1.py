class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxnum=0
        while(i<j):
            mul=(j-i)*min(heights[i],heights[j])
            if(mul>maxnum):
                maxnum=mul
            if(heights[i]<heights[j]):
                i+=1
            else:
                j-=1
        return maxnum

        