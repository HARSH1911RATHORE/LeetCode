class Solution:
    def ispalindrome(self, s, l, r):
        while l<r:
            if self.tolow(s[l])!=self.tolow(s[r]):
                return False
            l+=1
            r-=1
        return True
    
    def alphanum(self, s)->bool:
        return ((s>='A' and s<='Z') or (s>='a' and s<='z') or (s>='0' and s<='9'))
    
    def tolow(self, s):
        # if (s>='A' and s<='Z'):
        #     return (s-'A'+'a')
        # return s
        return s.lower()

    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            while (l<r and not self.alphanum(s[l])):
                l+=1
            while (l<r and not self.alphanum(s[l])):
                r-=1
            if s[l] != s[r]:
                return (self.ispalindrome(s, l+1, r)) or (self.ispalindrome(s, l, r-1))
            l += 1
            r -= 1
        return True

