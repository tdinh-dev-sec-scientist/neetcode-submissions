class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0, count1, count2 = 0, 0 , 0

        for n in nums:
            if n == 0:
                count0+=1
            elif n == 1:
                count1 +=1
            else:
                count2+=1
        i = 0
        for _ in range(count0):
            nums[i] = 0
            i+=1
        for _ in range(count1):
            nums[i] = 1
            i+=1
        for _ in range(count2):
            nums[i] = 2
            i+=1


