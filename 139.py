class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        DP = [False for _ in range(n+1)]
        DP[0] = True
        
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] in wordDict and DP[i]:
                    DP[j+1] = True
        return DP [-1]
