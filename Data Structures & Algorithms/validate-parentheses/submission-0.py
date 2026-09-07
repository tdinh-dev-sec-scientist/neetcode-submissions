class Solution:
    def isValid(self, s: str) -> bool:
        # 2 stacks: 1 is open and one is close
        stack = []

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ')' and top !='(': return False
                if c == ']' and top !='[': return False
                if c == '}' and top !='{': return False
        return len(stack) ==0



        