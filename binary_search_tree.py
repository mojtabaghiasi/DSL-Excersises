class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self , value):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while temp is not None:
            if(temp.value == value):
                return False
            if(value > temp.value):
                if(temp.right is None):
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if(temp.left is None):
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self, value):
        if(self.root is None):
            return False
        temp = self.root
        while(temp is not None):
            if(value > temp.value):
                temp = temp.right
            elif(value < temp.value):
                temp = temp.left
            else:
                return True
        return False
        
            
            



        