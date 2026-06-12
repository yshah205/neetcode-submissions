class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        beforeI = [1] * len(nums)
        afterI = [1] * len(nums)
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            beforeI[i] = beforeI[i-1] * nums[i-1]

        for i in range(len(nums) -2, -1, -1):
            afterI[i] = afterI[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            output[i] = beforeI[i] * afterI[i]

        return output