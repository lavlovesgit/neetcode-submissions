class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(arr, n, i):

            # Initialize largest as root
            largest = i

            # left index = 2*i + 1
            l = 2 * i + 1

            # right index = 2*i + 2
            r = 2 * i + 2

            # If left child is larger than root
            if l < n and arr[l] > arr[largest]:
                largest = l

            # If right child is larger than largest so far
            if r < n and arr[r] > arr[largest]:
                largest = r

            # If largest is not root
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]

                # Recursively heapify the affected sub-tree
                heapify(arr, n, largest)
        n=len(nums) 
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

    # Build heap (rearrange vector)
        for i in range(n-1, n-k-1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(nums, i, 0)
        return nums[n-k]

                
                
        