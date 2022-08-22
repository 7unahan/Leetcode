class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import numpy as np
        out_arr = nums1 + nums2
        out_arr.sort()
        if len(out_arr)%2 == 1:
            output1 = out_arr[len(out_arr)//2]
            return output1
        else:
            output2 = out_arr[(len(out_arr)//2)-1]+out_arr[(len(out_arr)//2)]       
            return output2/2.0
