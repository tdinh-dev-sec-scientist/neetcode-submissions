class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(pref):
                pref = pref[:-1]

                if pref == "":
                    return ""
        return pref