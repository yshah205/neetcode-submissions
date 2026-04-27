class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        match = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key in match:
                match[key].append(word)
            else:
                match[key]=[word] 
        return list(match.values())
        