OPEN_BRACKETS = {'(', '[', '{'}
CLOSE_BRACKETS = {')', ']', '}'}
BRACKETS_PAIRS = {')': '(', ']': '[', '}': '{'}

class Stack:
    
    def __init__(self) -> None:
        self.items = list()

    # Проверка стека на пустоту
    def isEmpty(self) -> bool:
        return not len(self.items)

    # Добавляет новый элемент на вершину стека. 
    def push(self, item) -> None:
        self.items.append(item)
    
    # Удаляет верхний элемент стека. Стек изменяется. 
    # Метод возвращает верхний элемент стека
    def pop(self):
        return self.items.pop(-1)
    
    # Возвращает верхний элемент стека, но не удаляет его. 
    # Стек не меняется.
    def peek(self):
        return self.items[-1]

    # Возвращает количество элементов в стеке.
    def size(self) -> int:
        return self.items.count()

def brackets_check_balanсed(brackets):
    if brackets is None:
        raise 'Строка не должна быть пустой!'
    
    stack = Stack()
    for bracket in brackets:
        if bracket in OPEN_BRACKETS:
            stack.push(bracket)
        elif bracket in CLOSE_BRACKETS:
            if stack.isEmpty():
                return 'Несбалансированно'
            last_bracket = stack.pop()
            if BRACKETS_PAIRS[bracket] != last_bracket:
                return 'Несбалансированно'
        else:
            raise 'Строка должна содержать только скобки!'
    
    if stack.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    input_str = input('Введите строку, содержащую только скобки:\n')
    print(brackets_check_balanсed(input_str))