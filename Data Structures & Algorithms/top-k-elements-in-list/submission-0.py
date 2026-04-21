class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]]=1+count.get(nums[i],0)
        arr=[]
        for i,c in count.items():
            arr.append([c,i])
        arr.sort()
        res=[]
        while len(res) < k:
            res.append(arr.pop()[1]) 
        return res       

                    