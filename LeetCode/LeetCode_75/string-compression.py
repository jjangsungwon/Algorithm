from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0
            
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        chars[:] = chars[:write]
        
        return write


if __name__ == "__main__":
    Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])