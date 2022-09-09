#traversal inorder, postorder, preorder
#class for creating the node
# sample tree

#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 8  11
#       /     \
#      16     25
#inorder traversal: [4,2,5,1,16,8,3,11,25]
#preorder traversal:[1,2,4,5,3,8,16,11,25]
#postorder traversal:[4,5,2,16,8,25,11,3,1]
class tree:
    def __init__(self, key):
        self.key= key
        self.left= None
        self.right=None

def parse(data):
    if isinstance(data, tuple) and len(data)==3:
        node= tree(data[1])
        node.left=parse(data[0])
        node.right=parse(data[2])
    elif data is None:
        node= None
    else:
        node=tree(data)
    return node


def inorder(node):
    if node is None:
        return []
    return(inorder(node.left) + [node.key] + inorder(node.right))

def preorder(node):
    if node is None:
        return []
    return([node.key] + preorder(node.left) + preorder(node.right))

def postorder(node):
    if node is None:
        return []
    return(postorder(node.left) + postorder(node.right) + [node.key])
tree_tuple=((4,2,5),1,((16,8,None),3,(None,11,25)))
tree=parse(tree_tuple)
print('inorder traversal = ',inorder(tree))
print('preorder traversal = ',preorder(tree))
print('postorder traversal = ',postorder(tree))

















