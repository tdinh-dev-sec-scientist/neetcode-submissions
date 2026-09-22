class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        prevMap={}
        for i, n in enumerate(nums):
            if n in prevMap:
                if i - prevMap[n] <= k:
                    return True
            prevMap[n]= i
        return False


        