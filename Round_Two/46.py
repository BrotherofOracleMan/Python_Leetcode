class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(left,k,arr,ans):
            if left == k:
                ans.append(list(arr))
            for i in range(left, k):
                arr[left], arr[i] = arr[i], arr[left]
                backtrack(left + 1,k , arr, ans)
                arr[left] , arr[i] = arr[i], arr[left]
        ans = []
        backtrack(0,len(nums), nums, ans)
        return ans
