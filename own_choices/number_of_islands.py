# https://leetcode.com/problems/number-of-islands/
# study this: https://www.techiedelight.com/es/breadth-first-search/

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

####################################################

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        # Edge case: empty grid
        if not grid:
            return 0

        # set matrix dim
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0
        
        def bfs(r,c):
            # iterative way, less memory, much efficiency 

            queue = list()
            visited.add((r,c))
            queue.append((r,c))

            while len(queue) != 0:
                row,col = queue.pop(0)

                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r,c = row + dr , col + dc
                    if ( r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visited ):

                        queue.append((r,c))
                        visited.add((r,c))





            pass


        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and (i,j) not in visited:

                    bfs(i,j)
                    islands +=1

        print(islands)
        return islands
     
  

if __name__ == "__main__":

    input_1 = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
              ]

    input_2 = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
              ]


    sol = Solution()
    sol.numIslands(input_2)