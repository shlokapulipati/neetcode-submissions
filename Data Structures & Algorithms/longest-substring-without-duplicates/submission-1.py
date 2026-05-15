class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=[False]*128
        l=0
        maxLen=0
        for r in range(len(s)):
            while seen[ord(s[r])]:
                seen[ord(s[l])]=False
                l+=1
            seen[ord(s[r])]=True
            maxLen=max(maxLen,r-l+1)
        return maxLen