class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for val in nums:
            hashMap[val] = hashMap.get(val,0) + 1

        res = 0
        for freq in hashMap:
            if hashMap[freq] > res and hashMap[freq] > (len(nums)//2):
                res = freq

        return res