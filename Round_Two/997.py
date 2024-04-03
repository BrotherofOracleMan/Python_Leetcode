class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degrees = [0] * (n+1)
        out_degrees = [0] * (n+1)
        town_judge = -1 

        for value in trust:
            in_degrees[value[1]]+=1
            out_degrees[value[0]]+=1

        for i in range(1,n+1):
            if out_degrees[i] == 0 and in_degrees[i] == n-1:
                town_judge = i
                break

        return town_judge
