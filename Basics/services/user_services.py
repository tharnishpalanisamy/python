from Basics.models.User import User
import datetime
from pathlib import Path 


user_path = Path('./data/data.json') 

print(user_path.exists())

class UserService:
    def __init__(self) : 
        pass 

    def create_user(self , name:str ,email:str ,  ) -> bool  : 
        pass

    def get_all_users(self) -> list[dict] :
        pass 

    def get_user_by_id(self,id) -> User :
        pass 

    def delete_user(self , id) ->bool : 
        pass 