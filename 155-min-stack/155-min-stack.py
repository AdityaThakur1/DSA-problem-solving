class Node:
    def __init__(self, data, mins):
        self.data = data
        if mins != None:
            self.minstack = min(mins, data)
        else:
            self.minstack = data
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None
        self.val = None

    def push(self, val: int) -> None:
        if self.head == None:
            obj = Node(val,None)
            self.head = obj
        else:
            curmin = self.getMin()
            obj = Node(val, curmin)
            obj.next = self.head
            self.head = obj

    def pop(self) -> None:
        if(self.head != None):
            self.val = self.head.data
            self.head = self.head.next
        return self.val

    def top(self) -> int:
        if(self.head != None):
            self.val = self.head.data
        return self.val

    def getMin(self) -> int:
        if(self.head != None):
            self.val = self.head.minstack
        return self.val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()