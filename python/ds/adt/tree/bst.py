class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        node = self.search(data)
        # no duplicates
        if node:
            return
        else:
            new_node = Node(data)
            if data <=node.data:
                node.left = new_node
            else:
                node.right = new_node


    def search(self,data):
        temp = self.root
        parent = temp
        while temp != None and temp.data != data:
            parent = temp
            if data <=temp.data:
                temp=temp.left
            else:
                temp = temp.right
        if temp:
            return temp
        else:
            return parent
