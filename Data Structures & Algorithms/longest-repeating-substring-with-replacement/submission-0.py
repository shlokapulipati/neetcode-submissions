class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=[0]*26
        l=0
        maxLen=0
        maxFreq=0
        for r in range(len(s)):
            index=ord(s[r])-ord('A')
            count[index]+=1
            maxFreq=max(maxFreq,count[index])
            while (r-l+1)-maxFreq>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen
            
            