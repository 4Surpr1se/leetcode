class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        if self.min_stack and val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.insert(0, val)
        if not self.min_stack:
            self.min_stack.append(val)
        self.stack.append(val)
        """
        :type val: int
        :rtype: None
        """

    def pop(self):
        if self.min_stack and self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        """
        :rtype: None
        """

    def top(self):
        return self.stack[-1] if self.stack else None
        """
        :rtype: int
        """

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
        """
        :rtype: int
        """


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())
