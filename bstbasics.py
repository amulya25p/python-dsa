#binary search tree implementation

#    1
#   / \
#  2   3

class tree:
    def __init__(self, key):
        self.key= key
        self.left= None
        self.right=None

# node0=tree(1)
# node1=tree(2)
# node2=tree(3)
# node0.left=node1
# node0.right=node2
# print(node0.key)
# print(node0.left.key)
# print(node0.right.key)

                                    #       1
                                    #      / \
                                    #     2   3
                                    #    / \   \
                                    #   4   5   6
                                    #          / \
                                    #         7   8  

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

tree_tuple=((4,2,5),1,(None, 3,(7,6,8)))
tree2=parse(tree_tuple)

print('root node==',tree2.key)

print('level 1')
print(tree2.left.key,tree2.right.key)

print('level 2')
print(tree2.left.left.key, tree2.left.right.key, tree2.right.left, tree2.right.right.key)

print('level 3')
print(tree2.right.right.left.key,  tree2.right.right.right.key)

