# Time: O(4^n/sqrt(n))
# Space: O(4^n/sqrt(n))

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open_cnt: int, closed_cnt: int) -> None:
            if len(stack) == n:
                result.append("".join(stack))
                return
            if open_cnt < n:
                stack.append("(")
                backtrack(open_cnt + 1, closed_cnt)
                stack.pop()
            if closed_cnt < open_cnt:
                stack.append(")")
                backtrack(open_cnt, closed_cnt + 1)
                stack.pop()

        backtrack(0, 0)
        return result


# Time: O(2^(2n)n)
# Space: O(2^(2n)n)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def generate() -> None:
            if len(stack) == 2 * n:
                if valid():
                    result.append("".join(stack))
            else:
                stack.append("(")
                generate()
                stack.pop()
                stack.append(")")
                generate()
                stack.pop()

        def valid() -> bool:
            count = 0
            for c in stack:
                if c == "(":
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        generate()
        return result
