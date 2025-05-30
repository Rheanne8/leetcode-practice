class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(0,len(nums)):
            left_sum = sum(nums[0:i])
            if left_sum == sum(nums) - left_sum - nums[i]:
                return i
        return -1
            


        '''
        left_ptr = 0
        right_ptr = len(nums)-1
        equal = 1
        while(equal):
            left_sum = sum(nums[0:left_ptr])
            print('left_sum: {}'.format(left_sum))
            print('left_ptr: {}'.format(left_ptr))

            right_sum = sum(nums[right_ptr:len(nums)])
            print('right_sum: {}'.format(right_sum))
            print('right_ptr: {}'.format(right_ptr))
           
            if right_ptr<=left_ptr :
                equal = 0
            if left_sum>right_sum:
                right_ptr -=1
            elif right_sum>left_sum:
                left_ptr +=1
            elif right_sum == left_sum:
                if(right_ptr == len(nums)-1):
                    right_ptr-=1
                else:
                    return left_ptr

        return -1
        '''

            
        

            


            

        