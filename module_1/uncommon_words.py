# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        
        l = s1.split() + s2.split()

        
        d = {i : 0 for i in l}

        for i in range(0,len(l)):
            d[l[i]]+=1

        return [i for i in l if d[i]==1]
       

        


if __name__ == "__main__":
    sol = Solution()
    print(sol.uncommonFromSentences("this apple is sweet", "this apple is sour"))