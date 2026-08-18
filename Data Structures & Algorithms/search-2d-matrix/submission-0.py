class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mi=len(matrix)
        n=len(matrix[0])
        l=0
        r=mi*n-1
        while(l<=r):
            m=l+(r-l)//2 
            i=m//n
            j=m%n
            if(target<matrix[i][j]):
                r=m-1
            elif(target>matrix[i][j]):
                l=m+1
            else:
                return True
        return False

        
            
        