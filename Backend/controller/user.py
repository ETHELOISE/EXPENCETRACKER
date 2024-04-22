# from models.user import User

print(User)
def save(id=None ,name=None ,email=None ,password=None):
        newUser = User(None ,name ,email ,password)
        newUser.save()

def get_user(id=None):
        result = User.read(id)
        print(result)
        return result

def delete_User(id):
        User.delete(id)
        

