class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", '-', "/", "*"}
        stack = []
        for token in tokens:
            if token in operands:
                n2 = stack.pop()
                n1 = stack.pop()
                if token == "*":
                    stack.append(n1 * n2)
                if token == "/":
                    stack.append(int(n1 / n2))
                if token == "+":
                    stack.append(n1 + n2)
                if token == "-":
                    stack.append(n1 - n2)
            else:
                stack.append(int(token))
        return stack[-1]
