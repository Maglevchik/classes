
class Queue:
    def enqueue(self, action): 
        self.queue.append(action)
        print(f"'{action}' добавлено в очередь.")
    
    def dequeue(self):
        for i in self.queue:
            print('очередь обработана и удалена из списка.') 
            self.queue.pop(0)
    
    def is_empty(self):
        if self.queue:
            print(True)
        else:
            print(False)
    
    def __init__(self):
        self.queue = []
user_inp = Queue()
a = input('input in queue:')
user_inp.enqueue(a)
b = input('input in queue:')
user_inp.enqueue(b)
c = input('input in queue:')
user_inp.enqueue(c)

user_inp.is_empty()
user_inp.dequeue()
print(user_inp)
user_inp.is_empty()