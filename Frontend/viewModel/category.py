# from models.category import Category

def save(id=None ,name=None ):
        Category.save(id)

def get_category(id=None):
        result = Category.read(id)
        print(result)
        return result

def delete_Category(id):
        Category.delete(id)
        
