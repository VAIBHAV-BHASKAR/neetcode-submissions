from collections import Counter 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        freq = Counter()
        n = len(s)
        for end in range(n):
            end_char = s[end]
            freq[end_char]+=1

            while freq[end_char]>1:
                start_char = s[start]
                freq[start_char]-=1
                start+=1
            longest = max(longest, end-start +1)
        
        return longest 