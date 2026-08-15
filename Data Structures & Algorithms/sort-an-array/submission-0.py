class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(l, m, r):
            i = l
            j = m + 1
            new = []

            # Merge the two sorted halves
            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    new.append(nums[i])
                    i += 1
                else:
                    new.append(nums[j])
                    j += 1

            # Remaining elements from left half
            while i <= m:
                new.append(nums[i])
                i += 1

            # Remaining elements from right half
            while j <= r:
                new.append(nums[j])
                j += 1

            # Put merged elements back into nums
            for k in range(len(new)):
                nums[l + k] = new[k]

        def merge_sort(l, r):
            if l >= r:
                return

            mid = (l + r) // 2

            merge_sort(l, mid)
            merge_sort(mid + 1, r)

            merge(l, mid, r)

        merge_sort(0, len(nums) - 1)

        return nums