class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        h_t = collections.defaultdict(int)
        odd_pairs = 0
        for c in s:
            h_t[c] +=1
        
        for value in h_t.values():
            if value%2 == 1:
                odd_pairs += 1
            if odd_pairs > 1:
                return False
        return True
        """
        h_t = [0] * 26
        count = 0
        for character in s:
            h_t[ord(character) - ord('a')] +=1
            if h_t[ord(character) - ord('a')]%2 == 0:
                count -=1
            else:
                count +=1
        return count <= 1
