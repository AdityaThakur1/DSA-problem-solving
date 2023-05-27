class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        l,r = 0,0
        ml = 1
        while(r<len(s)-1):
            if s[r+1] in set(s[l:r+1]):
                while(s[r+1] in set(s[l:r+1])):
                    l += 1
            r+=1
            ml = max ( ml, r-l+1)
            
            
        return ml
            