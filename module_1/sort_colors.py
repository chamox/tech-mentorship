# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            
            val = nums[i]
            j=i-1
            while (j>=0) and (val < nums[j]):
                nums[j+1]= nums[j]

                j-=1
            nums[j+1] = val

        return nums
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortColors([2,0,2,1,1,0]))