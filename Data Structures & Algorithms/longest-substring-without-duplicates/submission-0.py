class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        c = set()
        l = 0
        counter = 0

        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l = l + 1
            c.add(s[r])
            counter = max(counter, r-l+1)
        return counter
