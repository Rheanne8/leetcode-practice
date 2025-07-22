class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans = [[], []]
        repeat = []
        for i in nums1:
            flag = 0
            for j in nums2:
                if i == j:
                    flag = 0
                    repeat.append(i)
                    break
                else: 
                    flag = 1
            if flag ==1:
                ans[0].append(i)
        ans1 = [x for x in nums2 if x not in repeat]
        ans[1]=(ans1)
        ans =  [list(set(inner)) for inner in ans]
        return ans
                

        
        