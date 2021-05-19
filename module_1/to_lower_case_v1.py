# Some help: https://en.wikibooks.org/wiki/Python_Programming/Text
# Tip: remember ascii table
# I think this is more general

class Solution:
    def toLowerCase(self, str: str) -> str:

        lower_str = ""
        
        for i in range(0,len(str)):

            if ord(str[i]) >= 65 and ord(str[i]) <= 90:
                lower_str += chr(ord(str[i])+32)
                i+=1
            else:
                lower_str += str[i]
                i+=1              

        return lower_str
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.toLowerCase("HOLA"))