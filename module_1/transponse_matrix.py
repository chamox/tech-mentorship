# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        
        m = len(matrix)
        n = len(matrix[1])

        to_return = [[0 for j in range(0,n)] for i in range(0,m)]

       
        for r in range(0,m):

            for c in range(0,n):

                to_return[c][r] = matrix[r][c]
                                
        return to_return
 
if __name__ == "__main__":
    sol = Solution()
    sol.transpose([[1,2,3],[4,5,6],[7,8,9]])