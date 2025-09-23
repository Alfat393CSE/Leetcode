class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Split the version strings by "."
        v1_parts = version1.split(".")
        v2_parts = version2.split(".")
        
        # Find the maximum length
        n = max(len(v1_parts), len(v2_parts))
        
        # Compare revisions one by one
        for i in range(n):
            # If index exceeds, treat as 0
            num1 = int(v1_parts[i]) if i < len(v1_parts) else 0
            num2 = int(v2_parts[i]) if i < len(v2_parts) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        # All parts are equal
        return 0
