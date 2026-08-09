class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]
            # 1 1 2 6
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer