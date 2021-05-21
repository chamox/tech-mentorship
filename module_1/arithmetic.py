# https://leetcode.com/problems/add-digits/
# A recursive solution for this problem. 

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num != 0:
            sum+=num%10
            num = (num-num%10)//10

        if sum < 10:

            return sum
        else:
            return self.addDigits(sum)

if __name__ == "__main__":
    solution = Solution()
    print(solution.addDigits(38))
