# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x^y
        c=0
        
        while n !=0:
            if n&1==1:
                c+=1
                n>>=1
            else:
                n>>=1
        return c
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingDistance(1,4))