class MinStack(object):

    def __init__(self):
        self.items = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if len(self.items) == 0:
            self.items.append([value, value])
        else:
            mini = min(value, self.items[-1][1])
            self.items.append([value, mini])

    def pop(self):
        """
        :rtype: None
        """
        if len(self.items) == 0:
            return -1
        return self.items.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.items) == 0:
            return -1
        return self.items[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.items) == 0:
            return 0
        return self.items[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()