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


from random import randrange

tree = BST()
arr = [ randrange(101) for i in range(10)]
arr = [50,30,20,40,70,60,80]
dt = list(map(lambda z: str(z),sorted(list(set(arr)))))
print(" ".join(dt))
[tree.insert(i) for i in arr]
tree.print()
print(tree.get_height(tree.root))
print(tree.root.data)
print("Depth: ",tree.find_depth(tree.root, 30))
print("Height: ",tree.get_height_of_node(30))
# print(tree.root.data)
# 