from fastapi import FastAPI
from pydantic import BaseModel , Field

app = FastAPI() 

class Product(BaseModel) :
    name:str = Field(min_length=2) 
    price : float = Field(gt=0) 
    quantity : int = Field(ge=1)

@app.put('/products/{product_id}') 
def update_product(product_id:int ,product:Product, notify:bool = False  ) :
    return {
        'message' : 'updated' , 
        'product_id' : product_id,
        'notify' : notify , 
        'product' : product
    }

