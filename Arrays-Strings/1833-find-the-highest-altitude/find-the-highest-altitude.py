class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        alt = [0]*(len(gain))
     
        k=0
        for i in range(0,len(gain)):
            altitude = alt[i-1] + gain[k]
            alt[i] = altitude
            k+=1
        if(max(alt)<0):
            return 0
        else:
            return max(alt)
        