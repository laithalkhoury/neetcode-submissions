class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        curr_area = 0

        while i < j:
            new_area = min(heights[i], heights[j]) * (j - i)
            if new_area > curr_area:
                curr_area = new_area
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1
        
        return curr_area
