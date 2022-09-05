class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        """
        copy_of_nums1 = nums1[:m]
        i1,i2,i3 = 0,0,0
    
        while i3 < (m+n):
            if i2 >= n or (i1 < m and copy_of_nums1[i1] < nums2[i2]):
                nums1[i3] = copy_of_nums1[i1]
                i1 += 1
            else:
                nums1[i3] = nums2[i2]
                i2 += 1
            i3+=1
            
        return nums1
        """
        i3 = m + n -1
        i1 = m - 1
        i2 = n - 1
        
        while i3 >= 0:
            if i2 < 0:
                break
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[i3] = nums1[i1]
                i1-=1
            else:
                nums1[i3] = nums2[i2]
                i2 -=1
            i3-=1

