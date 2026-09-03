import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        arr = []

        for x, y in points:
            d = x**2 + y**2
            arr.append([d, [x, y]])

        def heapify(arr, n, i):
            smallest = i

            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l][0] < arr[smallest][0]:
                smallest = l

            if r < n and arr[r][0] < arr[smallest][0]:
                smallest = r

            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                heapify(arr, n, smallest)

        # Build min heap
        n = len(arr)
        res=[]


        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n-1, n-k-1, -1):
                res.append(arr[0][1])
                arr[0], arr[i] = arr[i], arr[0]
                
                heapify(arr, i, 0)
        return res
        


        