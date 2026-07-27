class Solution:
    def reverseWords(self, s: str) -> str:
        temp = []
        result = []

        for ch in s:
            if ch == " ":
                if temp:
                    result.append("".join(temp))
                    temp = []
            else:
                temp.append(ch)
            
        if temp:
            result.append("".join(temp))
        
        return " ".join(reversed(result))
        