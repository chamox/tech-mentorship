#~
# Cries in computer architecture.


class Solution:
    def findComplement(self, num: int) -> int:

        i=1

        while i<=num:
            num=num^i
            i=i<<1

        return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.findComplement(5))