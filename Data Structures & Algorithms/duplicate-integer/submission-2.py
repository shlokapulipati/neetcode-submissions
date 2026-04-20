class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset=set(nums);
        if len(nums)==len(dupset):
            return False
        return True