class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        """for i in range(len(temperatures)-1, -1, -1):
            #print(temperatures[i])
            break_out_flag = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.insert(0,(j-i))
                    break_out_flag = True
                    break
            if break_out_flag != True: 
                result.insert(0,0)
        
        return result"""
        
        de = collections.deque()
        de.appendleft(0)
        for i in range(1,len(temperatures)):
            while(de):
                if(temperatures[de[0]] < temperatures[i]):
                    idx =  de.popleft()
                    result[idx] =  i - idx
                else:
                    de.appendleft(i)
                    break
            de.appendleft(i)
        
        return result
                
        