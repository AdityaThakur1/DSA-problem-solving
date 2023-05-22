from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_dict:
            return ""
        
        val_array = self.key_dict[key]
        if(len(val_array) == 1):
            return val_array[0][0]
        
        if(val_array[0][1] > timestamp):
            return ""
        
        lt, rt = 0, len(val_array)-1
        prev_idx = 0
        while(lt <= rt):
            mid = (lt+rt)//2
            if(timestamp == val_array[mid][1]):
                return val_array[mid][0]
            elif (timestamp > val_array[mid][1]):
                prev_idx = max(prev_idx, mid)
                lt = mid + 1
            else:
                rt = mid - 1
        
        return val_array[prev_idx][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)