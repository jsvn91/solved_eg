class Queue():

    def __init__(self) -> None:
        self.l = []
    
    def is_empty(self):
        return (self.l.__len__()==0)

    def enqueue(self, elem):
        self.l.append(elem)
    
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            elem = self.l[0]
            self.l.remove(elem)
            return elem


q = Queue()
q.enqueue(2)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)

print("dequeue =", q.dequeue())
        