class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        n=len(res)
        if n%2==1:
            return res[n//2]
        else:
            mid1=res[n//2]
            mid2=res[n//2-1]
            return (mid1+mid2)/2
                


            
