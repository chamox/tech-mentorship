# Think pointers in C can help, sadly don't remember.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        i = 0

        while j>i:

            temp = s
            s[i],s[j] = temp[j],temp[i]

            i+=1
            j-=1        

if __name__ == "__main__":
    sol = Solution()
    sol.reverseString(["h","o","l","a"])