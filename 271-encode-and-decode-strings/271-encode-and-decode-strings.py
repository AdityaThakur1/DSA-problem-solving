class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        new_str = ""
        for st in strs:
            new_str += st + ":"
        return new_str



    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        result = []
        result = str.split(":")[0:-1]
        return result
