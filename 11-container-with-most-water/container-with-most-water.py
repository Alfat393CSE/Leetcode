class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)
            
            # Move the pointer of the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(Solution().maxArea([1,1]))  # Output: 1
