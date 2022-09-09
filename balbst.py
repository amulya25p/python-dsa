#check of balanced binary search tree

class user:
    def __init__(self, username, name, email):
        self.username=username
        self.name=name
        self.email=email
    
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

aakash = user('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = user('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = user('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = user('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = user('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = user('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = user('vishal', 'Vishal Goel', 'vishal@example.com')

users=[aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]


class bst_node:
    def __init__(self, key, value=None):
        self.key=key
        self.left=None
        self.right=None
        self.value=value    #contains the details of object
        self.parent=None    #pointer the parent node for easy traversal upwards

def insert(node, key, value):
    if node is None:
        node=bst_node(key, value)
    elif key<node.key:
        node.left=insert(node.left,key, value) 
        node.left.parent=node
    elif key>node.key:
        node.right=insert(node.right,key, value) 
        node.right.parent=node
    return node

#func to check the bst is balanced or not

def balance(node):
    if node is None:
        return True, 0
    bal_l, h_l=balance(node.left)
    bal_r, h_r=balance(node.right)

    bal=bal_l and bal_r and abs(h_l-h_r)<=1
    h=max(h_l,h_r)+1
    return bal, h

tree=insert(None, jadhesh.username, jadhesh)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

print(balance(tree))