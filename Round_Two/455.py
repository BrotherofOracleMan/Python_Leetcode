class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie_ptr, greed_ptr = len(s) - 1 , len(g) -1
        number_of_children_satisfied = 0

        while cookie_ptr  >= 0 and greed_ptr >= 0:
            if s[cookie_ptr] >= g[greed_ptr]:
                cookie_ptr-=1
                greed_ptr-=1
                number_of_children_satisfied += 1 
            elif g[greed_ptr] > s[cookie_ptr]:
                greed_ptr -= 1
        return number_of_children_satisfied
