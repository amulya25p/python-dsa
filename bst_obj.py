#bst operations insert, find, update, display all

from dis import dis


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

def display(node, space='\t', level=0):
    if node==None:
        print(space*level,'N')
        return
    elif node.left==None and node.right==None:
        print(space*level, str(node.key))
        return
    
    display(node.right, space, level+1)
    print(space*level + str(node.key))
    display(node.left,space, level+1)

#inertion function
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
#search function
def find(node, key):
    if node is None:
        print('node doesnt exist')
        return
    elif node.key==key:
        return node
    elif node.key>key:
        return find(node.left,key)
    elif node.key<key:
        return find(node.right,key)
 
#function for updating
def update(node,key, value):
    unode=find(node, key)
    if unode is not None:
        unode.value=value
    return unode

#function for listing the objects
def all_object(node):
    if node is None:
        return []
    return all_object(node.left) + [(node.key,node.value)] + all_object(node.right)

#manual insertion instance
# tree=bst_node(jadhesh.username, jadhesh)
# tree.left=bst_node(biraj.username, biraj)

#insertion usinf function
tree=insert(None, jadhesh.username, jadhesh)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)
node = find(tree, 'hemanth')
print(node.value)
unode=update(tree,'biraj', user('biraj','biraj chhaterjee','biraj@hotmail'))
print(unode.key)
print(unode.value.name)

print(all_object(tree))



