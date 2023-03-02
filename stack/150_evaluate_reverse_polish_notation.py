# n=len(tokens)
# Time: O(n)
# Space: O(n)

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if stack and token in operators:
                operator = token
                operand2 = stack.pop()
                operand1 = stack.pop()
                if operator == "+":
                    stack.append(operand1 + operand2)
                elif operator == "-":
                    stack.append(operand1 - operand2)
                elif operator == "*":
                    stack.append(operand1 * operand2)
                elif operator == "/":
                    stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))
        return stack[-1]
