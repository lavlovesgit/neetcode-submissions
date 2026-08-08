class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxvol=0
        while(l<r):
            vol=(r-l)*(min(heights[l],heights[r]))
            if(vol>maxvol):
                maxvol=vol
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
            

        return maxvol


        