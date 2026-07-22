class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                 vowels.append(s[i])
        
        index = -1
        result = ""
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                result += vowels[index]
                index += -1
            else:
                result += s[i]
        
        return result