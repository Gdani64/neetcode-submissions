class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) < 2):
            return False

        parenthesis_set = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for c in s:
            if c in parenthesis_set:
                if len(stack) > 0 and stack[-1] == parenthesis_set[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        print(stack)
        return len(stack) == 0