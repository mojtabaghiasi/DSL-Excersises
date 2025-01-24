class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while(temp is not None):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if(self.length == 0):
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if(self.length == 0):
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if(self.length == 0):
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if(self.length == 0):
            self.tail = None
        return temp
    
    def get(self, index):
        if(index > self.length - 1 or index < 0):
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if(temp):
            temp.value = value
            return True
        else:
            return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if(index == 0):
            return self.pop_first()
        if(index == self.length - 1):
            return self.pop()
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



## Exapmles of DSL questions

def find_middle_node(self):
    slowTemp = self.head
    fastTemp = self.head
    while(fastTemp is not None and fastTemp.next is not None):
        slowTemp = slowTemp.next
        fastTemp = fastTemp.next.next
    return slowTemp

def has_loop(self):
    slow = self.head
    fast = self.head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    return False

def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if(fast is None):
            return None
        fast = fast.next
    while(fast is not None):
        fast = fast.next
        slow = slow.next
    return slow

def partition_list(self , x):
    if(self.head is None):
        return
    less_head = Node(0)
    greater_head = Node(0)
    less = less_head
    greater = greater_head

    current = self.head
    while current is not None:
        if current.value < x:
            less.next = current
            less = current
        else:
            greater.next = current
            greater = current
        current = current.next
    greater.next = None
    less.next = greater_head.next
    self.head = less.next


def remove_duplicates(self):
    if(self.head is None):
        return
    values = set()
    previous = None
    current = self.head
    while current is not None:
        if(current.value in values):
            previous.next = current.next
            self.length -= 1
        else:
            values.add(current.value)
            previous = current
        current = current.next


def binary_to_decimal(self):
    num = 0
    current = self.head
    while current is not None:
        num = num * 2 + current.value
        current = current.next
    return num

def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    before = None
    after = temp.next
    for _ in range(self.length):
        temp.next = before
        before = temp
        temp = after
        after = after.next
        