class Solution:
    def isanagram(self, q1, q2):
        return sorted(q1) == sorted(q2)
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        
        l= 0
        r = l1
        
        while(r <= l2):
            if self.isanagram(s1, s2[l:r]):
                return True
            else:
                l, r = l+1, r+1
        
        return False