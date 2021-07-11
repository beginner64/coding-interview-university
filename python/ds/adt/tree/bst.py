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

    def get_height(self,node):
        #  max depth = height
        if node == None:
            # single node's height is 1 then do 0
            return -1
        else:
            return max(self.get_height(node.left),self.get_height(node.right))+1

    def get_height_of_node(self,data):
        node = self.search(data)
        return self.get_height(node)

    def find_depth(self,node, x):
        # Base case
        if (node == None):
            return -1
    
        # Initialize distance as -1
        dist = -1
    
        # Check if x is current node=
        if (node.data == x):
            return dist + 1
    
        dist = self.find_depth(node.left, x)
        if dist >= 0:
            return dist + 1
        dist = self.find_depth(node.right, x)
        if dist >= 0:
            return dist + 1
        return dist

    def delete_node(self,value):
        temp = self.root
        parent = None
        is_left = True
        while temp != None and temp.data != value:
            parent = temp
            if value <=temp.data:
                temp=temp.left
                is_left= True
            else:
                temp = temp.right
                is_left= False
        # return if the key is not found in the tree
        if temp is None:
            return
        node = temp
        # node has 1 child
        #node has 2 child
        #node has no child
        if node.left == None and node.right == None:
            if node != self.root:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        elif node.left == None or node.right == None:
            if node.left:
                child = node.left
            else:
                child = node.right
            if child != self.root:
                if is_left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root=child
        else:
            successor = self.find_successor_for_delete(node)
            if node != self.root:
                if is_left:
                    parent.left = successor
                else:
                    parent.right = successor
            else:
                self.root = successor
            successor.left = node.left
            
            
    def find_successor_for_delete(self,node):
        s_p = node
        s = node.right 
        while s!= None and s.left!=None:
            s_p=s
            s = s.left
        if(s != node.right):
            s_p.left =s.right
            s.right = node.right
        return s               
# python program to delete a tree
    def delete_tree(self,root):
        if root ==None:
            return 
        root.left =self.delete_tree(root.left)
        root.right =self.delete_tree(root.right)
        if root == self.root:
            self.root=None
            print("it is root")
        root = None

from random import randrange

tree = BST()
arr = [ randrange(101) for i in range(10)]
arr = [50,30,20,40,70,60,80,75,72,78,73]
dt = list(map(lambda z: str(z),sorted(list(set(arr)))))
print(" ".join(dt))
[tree.insert(i) for i in arr]
tree.print()
print(tree.get_height(tree.root))
print(tree.root.data)
print("Depth: ",tree.find_depth(tree.root, 90))
print("Height: ",tree.get_height_of_node(30))
tree.delete_node(50)
tree.print()
print()
print(tree.root.data)
tree.delete_node(70)
tree.print()
print()
print(tree.root.data)
print("deleting tree")
tree.delete_tree(tree.root)
print("printing tree")
tree.print()
# print(tree.root.data)
# 
