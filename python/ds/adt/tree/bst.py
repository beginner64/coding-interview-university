class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.s=0

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
            self.s+=1


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
    
    def is_in_tree(self,data):
        return self.search(data) != None

    def get_node_count():
        return self.s

    def get_min():
        temp = self.root
        while temp!=None and temp.left:
            temp = temp.left
        return temp

    def get_max():
        temp = self.root
        while temp!=None and temp.right:
            temp = temp.right
        return temp

    # def in_order_print():
