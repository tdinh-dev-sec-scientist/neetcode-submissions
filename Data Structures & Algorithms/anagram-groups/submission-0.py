class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1 . recognize: anagram
        #2; group
        groups = {}
        
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:
                groups[key] = []

            groups[key].append(s)
        return list(groups.values())




        
        