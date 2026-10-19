class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            for item in reversed(top.getList()):
                self.stack.append(item)
        return False