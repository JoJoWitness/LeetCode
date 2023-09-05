

# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
     
#         hashDict = {}
#         result = []

#         def createTestDict(string):
#             strDict = {}
#             for i in range(len(string)):
#                 if string[i] in strDict:
#                     strDict[string[i]] += 1
#                 else:
#                     strDict[string[i]] = 1
#             return strDict

#         for i in range(len(strs)):
             
#             testDict = createTestDict(strs[i])

    
#             if hashDict:
            
#                 for j in hashDict:
#                     if testDict == hashDict[j]:
#                         result[int(j)].append(strs[i])
#                         break

#                     elif j == str(len(hashDict) - 1):
#                         hashDict[str(len(result))] = testDict 
#                         result.append([strs[i]])
#                         break
                
                   
#             else:
#                 hashDict["0"] = testDict
#                 result.append([strs[i]])
        
#         print(hashDict)


            
            
        





       