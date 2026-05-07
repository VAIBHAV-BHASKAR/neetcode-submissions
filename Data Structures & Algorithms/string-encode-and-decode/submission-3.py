class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""
        
        for word in strs:
            
            length = str(len(word)).zfill(3)
            
            result += length + word
        
        return result


    def decode(self, s: str) -> List[str]:
        
        result = []
        
        i = 0
        
        while i < len(s):
            
            length = int(s[i:i+3])
            
            word = s[i+3 : i+3+length]
            
            result.append(word)
            
            i = i + 3 + length
        
        return result