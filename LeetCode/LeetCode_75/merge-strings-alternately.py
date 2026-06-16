class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for i in range(min(len(word1), len(word2))):
            output += word1[i] + word2[i]
        return output + word1[len(word2):] + word2[len(word1):]


if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeAlternately("abc", "pqr"))
    print(solution.mergeAlternately("ab", "pqrs"))
    print(solution.mergeAlternately("abcd", "pq"))