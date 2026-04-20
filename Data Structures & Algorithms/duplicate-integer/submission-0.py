class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset=set();
        for i in nums:
            if i in dupset:
                return True
            dupset.add(i)
        return False