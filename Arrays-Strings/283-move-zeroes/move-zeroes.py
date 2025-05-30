class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i=0
        count = 0
        while(count<length):
            if(nums[i]==0):
                nums.append(0)
                del nums[i]
                
            else:
                i+=1
            count+=1
        return nums
        
