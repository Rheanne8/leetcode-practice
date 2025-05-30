class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        curr1 = word1[i]
        curr2 = word2[i]
        len1 = len(word1)
        len2  = len(word2)
        final = ''
        if(len1 <= len2):
            while(i<(len1)):
                final = final + curr1 + curr2 
                i+=1
                if(i==len1):
                    break
                curr1 = word1[i]
                curr2 = word2[i]
                print(final)
            final = final + word2[i:]
        if(len2 < len1):
            while(i<(len2)):
                final = final + curr1 + curr2 
                i+=1
                if(i==len2):
                    break
                curr1 = word1[i]
                curr2 = word2[i]
            final = final + word1[i:]
        return final

        