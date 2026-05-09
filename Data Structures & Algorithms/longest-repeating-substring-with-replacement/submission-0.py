class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxfreq = 0
        start=0
        longest = 0
        n = len(s)
        for end in range (n):
            freq[s[end]]=1+freq.get(s[end], 0)
            maxfreq= max(maxfreq, freq[s[end]])

            while (end - start + 1) - maxfreq>k:
                freq[s[start]]-=1
                start +=1

            longest = max (longest, end - start + 1)
        return longest 