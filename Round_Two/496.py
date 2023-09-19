class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        values_dict = dict()
        ans = []

        for value in nums2:
            values_dict[value] = -1

        for elem in nums2:
            while len(stack) and elem > stack[-1]:
                values_dict[stack[-1]] = elem
                stack.pop()
            stack.append(elem)

        for val in nums1:
            ans.append(values_dict[val])

        return ans
