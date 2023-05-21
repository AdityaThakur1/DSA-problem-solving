class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rownum = -1
        for row in matrix:
            if(row[0] <= target):
                rownum += 1
            else:
                break
                
        l,r = 0, len(matrix[0])-1
        #print(l,r)
        while(l<=r):
            mid = (l+r)//2
            print(matrix[rownum][mid])
            if(matrix[rownum][mid] ==  target):
                return True
            elif (matrix[rownum][mid] <  target):
                l = mid + 1 
            else:
                r = mid - 1
                
        return False