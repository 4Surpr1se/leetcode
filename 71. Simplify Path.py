class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path = path.split('/')
        for i in path:
            if i == '..':
                if stack:
                    stack.pop(-1)
                else:
                    pass
            elif i not in ['.', '']:
                stack.append(i)
        return '/' + '/'.join(stack)

print(Solution().simplifyPath("/a//b////c/d//././/.."))
