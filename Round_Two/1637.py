class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_vertical_area = 0

        point_list = sorted(list(set(point[0] for point in points)))
        print(point_list)
        for i in range(len(point_list) - 1):
            max_vertical_area = max(max_vertical_area, point_list[i+1] - point_list[i])
        return max_vertical_area
