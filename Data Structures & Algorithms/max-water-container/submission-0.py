class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = 0
        n = len(heights)
        i=0
        j=n-1

        while i<j:
            vol = (j-i) * min(heights[j], heights[i])
            maxvol = max(vol, maxvol)
            if heights[i]<heights[j]:
                i+=1
            else :
                j-=1
            
        return maxvol