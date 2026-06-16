class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        stringOne = {}
        windowMap = {}

        for i in range(len(s1)):
            if s1[i] not in stringOne:
                stringOne[s1[i]] = 0
            stringOne[s1[i]] += 1
            
        l = 0
        for r in range(len(s2)):
            if s2[r] not in windowMap:
                windowMap[s2[r]] = 0
            windowMap[s2[r]] += 1

            while r-l+1> len(s1):
                windowMap[s2[l]] -= 1
                if windowMap[s2[l]] == 0: del windowMap[s2[l]]
                l += 1
            if windowMap == stringOne:
                return True
        return False
