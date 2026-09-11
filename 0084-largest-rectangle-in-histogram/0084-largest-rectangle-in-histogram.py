class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):

            if i == len(heights):
                current_height = 0
            else:
                current_height = heights[i]

            while stack and heights[stack[-1]] > current_height:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area
        