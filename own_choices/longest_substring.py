# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # we are going to hash all our sub strings
        words = dict()

        sub_string = ""
        words[s[0]] += len(sub_string)

        for i in range(len(s)):
            self.verify_chars()
            candidate = sub_string + s[i]

            
            
     
        
    def verify_chars(self, char: str, word: str):

        for i in range(len(word)):
            if word[i]==char:
                return True
        return False

       





if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))

    print(sol.verify_chars("a","abcabcbb"))