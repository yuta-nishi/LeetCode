# n=len(s)
# Time: O(n)
# Space: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_parentheses = {"}": "{", "]": "[", ")": "("}
        for c in s:
            if c in dict_parentheses:
                if stack and stack[-1] == dict_parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
