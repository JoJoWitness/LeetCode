class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sDict = {}
        tDict= {}

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in sDict:
                    sDict[s[i]] += 1
                else:
                    sDict[s[i]] = 1

                if t[i] in tDict:
                    tDict[t[i]] += 1
                else:
                    tDict[t[i]] = 1
        else:
            return False
        
        for i in sDict:
            if i in tDict and sDict[i] == tDict[i] :
                continue
            else:
                return False   
        return True