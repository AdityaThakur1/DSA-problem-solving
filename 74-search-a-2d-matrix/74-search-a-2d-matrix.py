class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        mid = 0
        found = 0
        
        while(l<=r):
            mid = (l+r)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                found = 1
                break
            elif matrix[mid][-1] < target:
                l = mid+1
            elif matrix[mid][0] > target:
                r = mid - 1
        
        if found == 0:
            return False
        
        l, r = 0, len(matrix[mid])-1
        row = mid
        
        while(l<=r):
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        
                