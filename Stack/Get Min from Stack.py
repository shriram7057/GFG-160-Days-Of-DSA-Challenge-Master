class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack=[]
        self.min_stack=[]
    
    def push(self, x):
        # Add an element to the top of Stack
        self.stack.append(x)
        if not self.min_stack or x<=self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        # Remove the top element from the Stack
        if self.stack:
            top=self.stack.pop()
            if top==self.min_stack[-1]:
                self.min_stack.pop()
            return top
        return -1
    
    def peek(self):
        # Returns top element of Stack
        if self.stack:
            return self.stack[-1]
        return -1
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack)==0
    
    def getMin(self):
        # Finds minimum element of 
        if self.min_stack:
            return self.min_stack[-1]
        return -1