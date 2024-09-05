class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
            }
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if not stack or brackets[stack.pop()] != i:
                    return False
        return not stack
