class MinStack:

    def __init__(self):
        self.stack = []  
        self.twostack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.twostack:
            self.twostack.append(val)
        else: 
            self.twostack.append(min(val, self.twostack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.twostack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.twostack[-1]
        
