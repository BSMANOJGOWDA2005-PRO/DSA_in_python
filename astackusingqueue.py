from collections import deque
class stack_using_que:
    def __init__(self):
        self.queue=deque()
    def push(self,item):
        self.queue.append(item)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
            


s = stack_using_que()
s.push(10)
s.push(20)
s.push(30)
print(s.queue)
    
