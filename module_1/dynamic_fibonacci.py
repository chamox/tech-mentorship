# https://leetcode.com/problems/fibonacci-number/

# A Dynamic Programming POV of fib sec


class Solution:
    def fib(self, n, mem={0:0, 1:1}):

        # if we have our current fib num in mem
        if n in mem:
            return mem[n]

        # otherwise we need to save it
        mem[n] = self.fib(n-1, mem) + self.fib(n-2, mem)

        return mem[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(300))