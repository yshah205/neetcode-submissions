class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        for ch in s:
            if ch in countS:
                countS[ch] = countS[ch] + 1
            else:
                countS[ch] = 1

        for ch in t:
            if ch in countT:
                countT[ch] = countT[ch] + 1
            else:
                countT[ch] = 1
    
        if countT == countS:
            return True
        else:
            return False


        
