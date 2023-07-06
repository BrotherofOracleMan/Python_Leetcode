class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageScorePairList = list(zip(ages, scores))
        DP = [0] * len(scores)
        n = len(ageScorePairList)

        ageScorePairList.sort()

        for i in range(n):
            DP[i] = ageScorePairList[i][1]
            
        for end_index in range(n):
            for start_index in range(end_index-1 ,-1,-1):
                if ageScorePairList[end_index][1] >= ageScorePairList[start_index][1]:
                    DP[end_index] = max(DP[end_index], DP[start_index] + ageScorePairList[end_index][1])
        return max(DP)
