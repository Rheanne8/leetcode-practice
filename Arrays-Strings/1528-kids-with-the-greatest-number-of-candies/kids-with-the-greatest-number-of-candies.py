class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        biggest_num = max(candies)
        arraylen = len(candies)
        #get the largest number in the array
        addCandies = [i+extraCandies for i in candies]
        #print(addCandies)
        result = []
        '''
        for i in range(0,arraylen):
            if(candies[i]> biggest_num):
                biggest_num = candies[i]
                #print(biggest_num)
        '''

        for i in range(0, arraylen):
            if(addCandies[i] >= biggest_num):
                result.append(True)
            else:
                result.append(False)
        return result
        
        