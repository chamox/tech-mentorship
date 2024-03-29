# https://leetcode.com/problems/add-digits/
# A recursive solution for this problem. 
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Input: num = 38
# Output: 2

# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# First of all, I 

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num != 0:
            sum+=num%10 # we sum the last digit of the num. Now we need to update the num
            num = (num-num%10)//10 # we remove the last digit. repeat until 0

        if sum < 10:

            return sum
        else:
            return self.addDigits(sum)

if __name__ == "__main__":
    solution = Solution()
    print(solution.addDigits(38))
