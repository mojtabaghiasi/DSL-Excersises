class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return False
        temp = self.top
        self.top = self.top.next
        temp.next =  None
        self.length -= 1
        return temp
    
# stack by list
class StackByList:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if(len(self.stack_list) == 0):
            return None
        return self.stack_list.pop()
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
    

## Exapmles of DSL questions

def is_balanced_parentheses(parantheses):
    stack = Stack()
    for char in parantheses:
        if(char == '('):
            stack.push(char)
        elif(char == ')'):
            if(stack.length == 0 ):
                return False
            stack.pop()
    return stack.length == 0
        
    
def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_string = ''
    for _ in range(stack.length):
        char = stack.pop().value
        reversed_string += char
    return reversed_string



def sort_stack(stack):
    sort_stack = Stack()
    while not temp.is_empty():
        temp = stack.pop()
        while( not sort_stack.is_empty() and sort_stack.peek() > temp):
            stack.push(sort_stack.pop())
        sort_stack.push(temp)        
    
    sortedTemp = sort_stack.pop()
    while sortedTemp is not None:
        stack.push(sortedTemp)

                






    
