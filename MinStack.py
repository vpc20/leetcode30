# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     getMin() -- Retrieve the minimum element in the stack.

# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:
    def __init__(self):
        self.arr = []
        self.min = 0

    def push(self, x: int) -> None:
        self.arr.append(x)
        if len(self.arr) == 1:
            self.min = self.arr[0]
        else:
            self.min = min(self.min, x)

    def pop(self) -> None:
        if len(self.arr) > 0:
            popval = self.arr.pop()
            if len(self.arr) == 0:
                self.min = None
            else:
                self.min = min(self.arr)

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # returns -3
minStack.pop()
print(minStack.top())  # returns 0
print(minStack.getMin())  # returns -2
