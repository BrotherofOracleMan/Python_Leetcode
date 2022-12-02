class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min_element(low, high):
            if nums[high] > nums[low]:
                return nums[low]
            while low <= high:
                pivot = low + (high-low)//2
                if nums[pivot] > nums[pivot +1]:
                    return nums[pivot +1]
                else:
                    if nums[pivot] >= nums[low]:
                        low = pivot + 1
                    else:
                        high = pivot - 1
                    print("low :{}".format(low))
                    print("high :{}".format(high))
        n = len(nums)
        if n == 1:
            return nums[0]

        return find_min_element(0,n-1)
