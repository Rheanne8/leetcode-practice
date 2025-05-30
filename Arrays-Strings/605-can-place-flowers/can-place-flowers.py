class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans = 0
        prev = -2
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                ans += max(0, (i - prev - 2) // 2) 
                prev = i
        ans += max(0, (len(flowerbed) - prev - 1) // 2)
        return ans >= n
        '''
        safe_space = 0
        j = 0
        length = len(flowerbed)
        #edge case 
        if(length == 1):
            if(flowerbed[j]==0 and n>1):
                return False
            elif(flowerbed[j]==1 and n>0):
                return False
            else:
                return True

        #for cases that end with 2 0s
        if(flowerbed[length-1] == 0 and flowerbed[length-2]==0):
            safe_space +=1
            flowerbed[length-1]=1 

        if(flowerbed[0]== 0 and flowerbed[1]==0):
                safe_space +=1  
                flowerbed[j]=1
        
        # Check first 2 positions 
        while(j+2<length-1):
            curr = flowerbed[j]
            third = flowerbed[j+2]

            if(curr==0 and third==0 and flowerbed[j+1]==0):
                safe_space +=1
                flowerbed[j+1] = 1

            
            j+=1
        print(safe_space)
        if safe_space>=n:
            return True
        else:
            return False
               
                

        '''
        '''
        total = 0
        
        i = 0
        j = 0
        start = flowerbed[j]
        length = len(flowerbed)
        for i in range(0, length):
            if (curr == 0):
                end = flowerbed[i]
            else:
                extract = flowerbed[j:i]

                j = i
                start = flowerbed[j]

        '''
          

