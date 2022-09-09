#function to check the given binary tree is bst

def max_min(pass_list):
    return [i for i in pass_list if i is not None]

#passed the list and returning the max and min in the list

def check_bst(node):
    if node is None:
        return True, None, None
    bst_l, min_l, max_l = check_bst(node.left)
    bst_r, min_r, max_r = check_bst(node.right)
    
    bst= (bst_l and bst_r and (max_l is None or max_l<node.key) and 
           (min_r is None or min_r>node.key))
    
    min_key=min(max_min([min_l, node.key, min_r]))
    max_key=max(max_min([max_l, node.key, max_r]))

    return bst, min_key, max_key

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

tree_tuple=((1,2,3),4,(5,6,7))
tree2=parse(tree_tuple)

print(check_bst(tree2))