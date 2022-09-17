class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        prev_list = ans[0]
        for i in range(1,numRows):
            current_list = []
            prev_list = ans[i-1]
            current_list.append(1)
            for x in range(1,len(prev_list)):
                current_list.append(prev_list[x] + prev_list[x-1])
            current_list.append(1)
            ans.append(current_list)
        return ans
