class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        countS=[0]*128
        countT=[0]*128
        for i in range(len(t)):
            countT[ord(t[i])]+=1
        need=0
        for val in countT:
            if val >0:
                need+=1
        l=0
        have=0
        res=[-1,-1]
        resLen=float("inf")
        for r in range(len(s)):
            countS[ord(s[r])]+=1
            if countS[ord(s[r])]==countT[ord(s[r])]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                countS[ord(s[l])]-=1
                if countS[ord(s[l])]<countT[ord(s[l])]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float("inf") else ""