class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.s=0

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
            return
        node = self.search(data)
        # no duplicates
        new_node = Node(data)
        if data ==node.data:
            return 
        elif data <node.data:
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

    def print(self):
        self.traverse_inorder(self.root)

    def traverse_inorder(self,root):
        if root == None:
            return 
        self.traverse_inorder(root.left)
        print(root.data, end = ' ')
        self.traverse_inorder(root.right)

from random import randrange

tree = BST()
arr = [ randrange(101) for i in range(10)]
dt = list(map(lambda z: str(z),sorted(list(set(arr)))))
print(" ".join(dt))
[tree.insert(i) for i in arr]
tree.print()
# print(tree.root.data)
