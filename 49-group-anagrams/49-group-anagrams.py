class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        res_dict = {}

        for s in strs:
            char_count = [0]*26
            for char in s:
                char_count[ord(char) - ord('a')]+= 1
            
            ct = tuple(char_count)
            if ct in res_dict:
                res_dict[ct].append(s)
            else:
                res_dict[ct] = [s]


        return list(res_dict.values())