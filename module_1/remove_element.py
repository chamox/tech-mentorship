# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        new_length = 0

        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[new_length] =nums[i] 
                new_length+=1

  
if __name__ == "__main__":
    sol = Solution()
    sol.removeElement([0,1,2,2,3,0,4,2],2)