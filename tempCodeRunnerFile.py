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
