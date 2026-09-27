class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum, right_sum = 0, sum(nums) - nums[0]

        if right_sum == 0:
            return 0
        
        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i
        
        return -1


if __name__ == "__main__":
    print(Solution().pivotIndex([1,7,3,6,5,6]))