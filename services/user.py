# user.py


from repositories.user import UserRepo


class UserService:

    def __init__(self):
        pass

    def authenticate_user(self,user_date):

        res= UserRepo().authenticate(user_date)
        print(res)
        return res
    def signup_user(self,user_data):
        data = {'Name': user_data['Name'], 'Id': int(user_data['Id']), 'Age': int(user_data['Age']),"Pwd":user_data["Pwd"]}
        return UserRepo().signup_user(data)



    def create_user(self, user_data):
        print(user_data['Id'])
        data = {'Name': user_data['Name'], 'Id': int(user_data['Id']), 'Age': int(user_data['Age'])}
        return UserRepo().save_user(data)

    def update_user(self,user_data):
        data = {'Name': user_data['Name'], 'Id': int(user_data['Id']), 'Age': int(user_data['Age'])}
        post_data = {'$set': data}
        UserRepo().update_user(int(user_data['Id']),post_data)

    def search_user(self,user_data):

        users= UserRepo().search_user(user_data['Name'])
        return list(users)

    def delete_user(self,user_data):
        UserRepo().delete_user(int(user_data))