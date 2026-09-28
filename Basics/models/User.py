from dataclasses import dataclass 
import datetime

@dataclass 

class User :
    id :  int 
    name : str 
    email : str 
    create_at : datetime 