from Basics.models.User import User
import datetime
from pathlib import Path 
import json 
from Basics.exceptions import UserNotFoundException , UserAlreadyExistsException


class UserService:
    def __init__(self) : 
        self.user_path = Path("./data/data.json") 

    def check_email_exists(self , email:str) ->bool : 
        all_users = self.get_all_users() 

        for user in all_users :
            if user['email'] == email :
                return True 
        return False 
    

    def create_user(self , user_name:str ,user_email:str  ) -> bool  :  
        email_exists = self.check_email_exists(user_email) 
        
        if email_exists :
            raise UserAlreadyExistsException(f"User with email {user_email} already exists")  
        
        all_users = self.get_all_users() 
        new_id = max((user['id'] for user in all_users ) , default=0) + 1 
        all_users.append({
            'id': new_id , 
            'name':user_name , 
            'email' : user_email , 
            'created_at' : datetime.datetime.now().isoformat()
        })

        with self.user_path.open('w') as file :
            json.dump(all_users , file , indent=4)
            return True  



    def get_all_users(self) -> list[dict] :
        with self.user_path.open('r') as file : 
            data = json.load(file)
            return data 

    def get_user_by_id(self,user_id:int) -> User   :
        all_users = self.get_all_users() 
        for user in all_users:
            if user['id'] == user_id :
                return User(
                    id = user['id'] , 
                    name = user['name'] , 
                    email = user['email'] , 
                    created_at = datetime.datetime.fromisoformat(
                                    user["created_at"]
                                )
                )
        raise UserNotFoundException(f'No user found with id {user_id}') 

    def delete_user(self , user_id : int ) ->bool : 
        found = False 
        all_users = self.get_all_users() 
        new_users = [] 
        for user in all_users :
            if user['id'] == user_id :
                found = True 
                continue 
            new_users.append(user) 
        with self.user_path.open('w') as file :
            json.dump(new_users , file , indent=4)
        return found  
