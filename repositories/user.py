
from . import posts

class UserRepo:

    def __init__(self):
        pass

    def authenticate(self,post_data):
        print(post_data)
        search = posts.find({'Name': post_data['Name'],'Pwd':post_data['Password']})
        for it in search:
            if it['Name']==post_data['Name'] and it['Pwd']==post_data['Password']:
                return True
        return False

    def signup_user(self,post_data):
        result = posts.insert_one(post_data)
        if result.inserted_id:
            print('One post: {0}'.format(result.inserted_id))
            return True
        else:
            return False


    def save_user(self, post_data):
        result = posts.insert_one(post_data)
        if result.inserted_id :
            print('One post: {0}'.format(result.inserted_id))
            return True
        else:
            return False
    def update_user(self,id,post_data):
        update = posts.update_one({"Id": id}, post_data)
        print(update)
        return update

    def search_user(self,name):
        search = posts.find({'Name': name})
        '''for it in search:
            print(it)'''
        #print("ds",search)
        return search

    def delete_user(self,id):
        delete = posts.remove({"Id": id})
        return delete


