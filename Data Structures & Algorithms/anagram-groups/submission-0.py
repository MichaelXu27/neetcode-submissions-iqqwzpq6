class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            ss = "".join(sorted(s))
            if ss in dic:
                dic[ss].append(s)
            else:
                dic[ss] = [s]

        ans = []
        for val in dic.values():
            ans.append(val)
        return ans