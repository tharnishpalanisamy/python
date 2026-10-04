# from fastapi import FastAPI 


# app =  FastAPI() 

# @app.get('/') 
# def home():
#     return{
#         'message':'Hello Home'
#     }

# @app.get('/about') 
# def get_about():
#     return{
#         'name' : 'tharnish' , 
#         'course' : 'Bsc Computer science with data analytics'
#     }


# @app.get('/skills') 
# def get_skills():
#     return[
#         'python' , 
#         'cpp' , 
#         'react' , 
#         'fastapi'
#     ] 

# @app.get('/status') 
# def get_status():
#     return {
#         'status' : 'running'
#     }

# @app.get('/users/{user_id}') 
# def get_user(user_id : int ) :
#     return{
#         'user_id' : user_id
#     }


from fastapi import FastAPI 

app = FastAPI() 

# @app.get('/products/{product_id}') 
# def get_product(product_id:int) :
#     return{
#         "product_id" : product_id , 
#         "message" : 'Product Found'
#     }


# @app.get('/students/{student_id}')
# def get_student(student_id:int) :
#     return{
#         'student_id':student_id , 
#         'message':'Student Found'
#     }


# @app.get('/users') 
# def get_user(limit:int|None = None , search:str|None = None) :
#     return{
#         'limit' : limit , 
#         'search' : search,
#         "message":'Ok'
#     }
 

@app.get('/products/{product_id}') 
def get_product(product_id : int , details : bool = False ) :
    return {
        'product_id' : product_id , 
        'details' : details
    }
