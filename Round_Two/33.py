class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(low,high):
            if nums[high] > nums[low]:
                return 0
            while low <= high:
                # find the highest number first
                pivot = low + (high - low)//2
                if nums[pivot] > nums[pivot +1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[low]:
                        high = pivot - 1
                    else:
                        low = pivot + 1
        
        def binarysearch(low, high):
            while low <= high:
                pivot = low + (high-low)//2
                if nums[pivot] == target:
                    return pivot
                else:
                    if nums[pivot] > target:
                        high = pivot-1
                    else:
                        low = pivot + 1
            return -1

        n = len(nums)
        if nums[0] == 0:
            return binarysearch(0, n- 1)
        if n == 1:
            return 0 if target == nums[0] else -1
        pivot = find_pivot(0, n-1)
        print(pivot)
        if nums[pivot] == target:
            return pivot

        if pivot == 0:
            return binarysearch(0, n-1)
        if target < nums[0]:
            return binarysearch(pivot, n-1)
        return binarysearch(0, pivot)
        

