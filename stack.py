class Stack:
    def push(self, action): # принимает действие (строку) и добавляет его в стек.
        self.stack.append(action)
    
    def pop(self): #удаляет и возвращает последнее добавленное действие из стека. Если стек пуст, выведите сообщение об этом
        if not self.stack:
            print("Стек пустой.")
            return None
        else:
            last_action = self.stack.pop() # Удаляем и получаем последний элемент
            print(f"'{last_action}' извлечена из стека.")
            return last_action
    
    def peek(self): # возвращает последнее действие без его удаления из стека. Если стек пуст, выведите сообщение об этом.
        if not self.stack:
            print("Стек пустой.")
            return None
        else:
            last_action = self.stack[-1] # Смотрим последний элемент без его удаления.
            print( last_action)
    
    def is_empty(self):
        if self.stack:
            print(True)
        else:
            print(False)
    
    def __init__(self):
        self.stack = []

box = Stack()
print("--- Изначальное состояние стека ---")
box.peek()
box.is_empty()
box.pop()

print("\n--- Добавляем строк ---")
box.push('Fox')
box.push('Bear')
box.push('Line')

print("\n--- Удаление предыдущего элемента ---")
box.pop()

print("\n--- Окончательный стек ---")
box.push('Wolf')
box.is_empty()
box.peek()
