# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        
        print("n:",n)

        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)


if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(4))