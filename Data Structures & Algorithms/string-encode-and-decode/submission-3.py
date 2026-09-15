class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        print("".join(encoded))
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        amount = 0
        ans = []
        total = []
        while i < len(s):
            if s[i] == "#":
                total = "".join(total)
                inc = int(total)
                ans.append(s[i+1:i+inc+1])
                i += inc
                total = []
            else:
                total.append(s[i])
            i += 1
        return ans


