class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        max = 0;
        c = set();
        for i in range(len(nums)):
            c.add(nums[i])
        for i in range(len(nums)):    
            if nums[i] - 1 not in c:
                conse = 1;
                while (nums[i]+conse) in c:
                    conse += 1
                if max < conse:
                    max = conse
        return max

