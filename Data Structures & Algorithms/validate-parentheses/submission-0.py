class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {"}": "{", "]": "[", ")": "("}
        stack = []
        for char in s: 
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            else:
                if not stack or stack[-1] != mappings[char]:
                    return False
                else:
                    stack.pop()
        return not stack
                
                
