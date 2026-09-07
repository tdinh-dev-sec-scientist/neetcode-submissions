class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in prev:
                return [prev[dif], i]
            
            prev[nums[i]] = i