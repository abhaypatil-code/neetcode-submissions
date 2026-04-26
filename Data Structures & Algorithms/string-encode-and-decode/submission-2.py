class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter '#'
            delim_pos = s.find('#', i)
            # Get the length of the upcoming string
            length = int(s[i:delim_pos])
            # Get the string itself
            str_content = s[delim_pos+1 : delim_pos+1+length]
            res.append(str_content)
            # Move the pointer to the start of the next length
            i = delim_pos + 1 + length
        return res