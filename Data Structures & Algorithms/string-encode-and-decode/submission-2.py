class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        
        return ''.join(encoded)

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        i = 0
        length = []
        while i < len(s):
            if s[i] != '#':
                length.append(s[i])
                i += 1
            else:
                intLength = int(''.join(length))
                decoded.append(s[i + 1: i + intLength + 1])
                i += 1 + intLength
                length = []

        return decoded

            
