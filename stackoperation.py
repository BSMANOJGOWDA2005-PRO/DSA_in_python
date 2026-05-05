class stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0

    def push_items(self, item):
        self.items.append(item)
        
    def pop(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items.pop()
    
    def top(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
      
s = stack()    
s.push_items(5)
s.push_items(9)
s.push_items(45)

print("stack contains:", s.items)
print("size of stack:", s.size())
print("top element of stack:", s.top())

print("popped element:", s.pop())
print("popped element:", s.pop())
print("popped element:", s.pop())

print("Is stack empty?", s.is_empty())