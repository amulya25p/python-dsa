#Write a function to calculate the height/depth of a binary tree
#Write a function to count the number of nodes in a binary tree

class tree:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None

def parse(data):
    if isinstance(data, tuple) and len(data)==3:
        node=tree(data[1])
        node.left=parse(data[0])
        node.right=parse(data[2])
    elif data is None:
        node= None
    else:
        node=tree(data)
    return node

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

def num_node(node):
    if node is None:
        return 0
    return 1 + num_node(node.left) + num_node(node.right)

tree_tuple=((4,2,5),1,((16,8,None),3,(None,11,25)))
tree=parse(tree_tuple)
print('tree height',tree_height(tree))
print('no of nodes in tree ', num_node(tree))

