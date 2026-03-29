class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []
        operations = {'+', '-', '/', '*'}
        for token in tokens:
            if token in operations:
                second = stack.pop()
                first = stack.pop()
                if token == '*':
                    stack.append(first * second)
                if token == '-':
                    stack.append(first - second)
                if token == '/':
                    stack.append(int(first / second))
                if token == '+':
                    stack.append(first + second)
                continue
            stack.append(int(token))
        return stack.pop()