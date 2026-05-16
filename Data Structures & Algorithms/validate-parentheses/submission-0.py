class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cp={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in cp:
                if stack and stack[-1]==cp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False