# Some help: https://en.wikibooks.org/wiki/Python_Programming/Text
# Tip: remember ascii table
# REMEMBER: ASCII TABLE, "A" -> POS 65, "a" -> POS 65+32  || "Z" -> POS 90 "z" -> POS 90+32

class Solution:
    def toLowerCase(self, str: str) -> str:
        lower_str = ""
        for c in str:

            if ord(c) >= 65 and ord(c) <= 90:
                lower_str += chr(ord(c)+32)
            else:
                lower_str += c              

        return lower_str
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.toLowerCase("PYTHONIC WAY"))