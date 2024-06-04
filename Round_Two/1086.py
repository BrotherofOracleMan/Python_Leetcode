class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        high_five_dict = defaultdict(list)
        ans = []
        items.sort()

        for id, score in items:
            high_five_dict[id].append(score)

        for key, value in high_five_dict.items():
            avg = int(sum(value[-5:])// 5 )
            ans.append([key, avg])
            
        return ans
