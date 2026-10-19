class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_cnt = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            
            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            
            max_length = max(max_length, right - left)

        return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))