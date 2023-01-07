class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmp,ans,i,tmp_sum):
            if tmp_sum > target:
                return
            if tmp_sum == target:
                ans.append(list(tmp))
                return
            for i in range(i,len(candidates)):
                tmp.append(candidates[i])
                backtrack(tmp,ans,i,tmp_sum + candidates[i])
                tmp.pop()
        ans = []
        backtrack([],ans,0,0)
        return ans
