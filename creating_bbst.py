#creating a balanced binary tree using array/list
class bst_node:
    def __init__(self, key, value=None):
        self.key=key
        self.left=None
        self.right=None
        self.value=value    #contains the details of object
        self.parent=None  

def create_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi=len(data)-1
    if lo>hi:
        return
    mid = (lo+hi)//2
    key, value=data[mid]
    root= bst_node(key,value)
    root.parent=parent
    root.left=create_bst(data, lo, mid-1, root)
    root.right=create_bst(data,mid+1,hi,root)
    return root
class user:
    def __init__(self, username, name, email):
        self.username=username
        self.name=name
        self.email=email
    
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

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


aakash = user('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = user('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = user('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = user('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = user('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = user('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = user('vishal', 'Vishal Goel', 'vishal@example.com')

users=[aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

data=[(user.username, user) for user in users]
print(data)
tree=create_bst(data,0)
print(display(tree))



