# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        d = dict()

        c=0

        for i in range(0,len(stones)):
            d[stones[i]]=0

        for i in range(0,len(jewels)):
            d[jewels[i]]=1

        for i in range(0,len(stones)):
            if d[stones[i]]==1:
                c+=1

        return c

if __name__ == "__main__":
    sol = Solution()
    print(sol.numJewelsInStones("aA","aAAbbbb"))

        