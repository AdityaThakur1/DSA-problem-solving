class Solution:    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        
        hm = [0]*26
        hm2 = [0]*26
        
        for c in s1:
            hm[ord(c) - ord('a')] += 1
            
        while(r<=len(s2)):
            if l == 0:
                for c in s2[l:r]:
                    hm2[ord(c) - ord('a')] += 1
                if hm == hm2:
                    return True
            else:
                hm2[ord(s2[l-1])- ord('a')] -= 1
                hm2[ord(s2[r-1])- ord('a')] += 1
                
                if hm == hm2:
                    return True
            l+=1
            r+=1
        
        return False
            