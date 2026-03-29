class Solution:

    def encode(self, strs: List[str]) -> str:
        self.lengths = []
        self.bigStr = ""
        for string in strs:
            length = len(string)
            self.lengths.append(length)
            self.bigStr += string
        return self.bigStr

    def decode(self, s: str) -> List[str]:
        self.ans = []
        self.output = ""
        last = 0
        for n in self.lengths:
            self.output = s[last:last + n]
            last += n
            self.ans.append(self.output)
        return self.ans

            
