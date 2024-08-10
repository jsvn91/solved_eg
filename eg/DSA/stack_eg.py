
class Stack():

    def __init__(self) -> None:
        self.l = []

    def add(self, elem):
        self.l.append(elem)
    
    def pop(self):
        if not self.l:
            print("stack empty")
        else:
            return self.l.pop()
    
    def is_empty(self):
        return self.l.__len__()==0


s = Stack()

s.add(1)
s.add(1)
s.add(1)
s.add(1)
s.add(2)

print("poped =", s.pop())