class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        commonPrefix=strs[0]
        
        while (commonPrefix!= strs[len(strs)-1][0:len(commonPrefix)]):
            commonPrefix=commonPrefix[0:len(commonPrefix)-1]
        return commonPrefix    
        
