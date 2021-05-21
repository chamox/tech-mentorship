# help at https://www.youtube.com/watch?v=6ysjqCUv3K4 
# https://leetcode.com/problems/binary-search/submissions/



class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left=0                  # first nums element index
        right=len(nums)-1       # last nums element index

        while left <= right:
            middle = (left+right)//2

            if nums[middle]==target:
                return middle
           
            elif target > nums[middle]:
                left=middle+1  

            else:
                right = middle-1

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,5], 5))