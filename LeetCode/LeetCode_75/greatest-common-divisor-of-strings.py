from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]


if __name__ == "__main__":
    solution = Solution()
    print(solution.gcdOfStrings("ABCABC", "ABC"))
    print(solution.gcdOfStrings("ABABAB", "ABAB"))
    print(solution.gcdOfStrings("LEET", "CODE"))