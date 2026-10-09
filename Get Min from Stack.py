class SpecialStack:

    def __init__(self):
        self.s = []
        self.min1 = None
        
    
    def push(self, x):
        if not self.s:
            self.min1 = x
            
        if self.min1 > x: 
            self.s.append(2*x - self.min1) #  < min, less on diff
            self.min1 = x
        else:
            self.s.append(x)

    
    def pop(self):
        if not self.s:
            return
            
        el = self.s.pop()
        if (el < self.min1):
            min2 = 2*self.min1 - el # restor pred min, plus more on diff
            self.min1 = min2

    
    def peek(self):
        if not self.s:
            return -1
        top = self.s[-1]
        if top < self.min1:
            return self.min1
        return top
        
    def isEmpty(self):
        return len(self.s) == 0

    
    def getMin(self):
        return self.min1 if self.s else -1