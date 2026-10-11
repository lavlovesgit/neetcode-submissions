class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(x,y):
            n=len(y)
            m=len(x)
            i=0
            j=0
            res=[]
            while(i<m and j<n):
                if x[i]<y[j]:
                    res.append(x[i])
                    i+=1
                else:
                    res.append(y[j])
                    j+=1
            while(i<m):
                res.append(x[i])
                i+=1
            while(j<n):
                res.append(y[j])
                j+=1
            return res






        def mergeSort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            x=mergeSort(arr[:mid])
            y=mergeSort(arr[mid:])
            return merge(x,y)
        return mergeSort(nums)

        
        