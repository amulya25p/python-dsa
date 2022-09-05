# define the class and insert the records
# perform insert, update, find,retrieve records operations

from collections import UserString

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

class UserDatabase:
    def __init__(self):
        self.users=[]
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users

a=UserDatabase()
for i in users:
    a.insert(i)
print(a.list_all())
a.update(user(username='hemanth', name='amulya', email='amulya@bcom'))

print(a.list_all())