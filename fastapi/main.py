from fastapi import FastAPI 


app =  FastAPI() 

@app.get('/') 
def home():
    return{
        'message':'Hello Home'
    }

@app.get('/about') 
def get_about():
    return{
        'name' : 'tharnish' , 
        'course' : 'Bsc Computer science with data analytics'
    }


@app.get('/skills') 
def get_skills():
    return[
        'python' , 
        'cpp' , 
        'react' , 
        'fastapi'
    ] 

@app.get('/status') 
def get_status():
    return {
        'status' : 'running'
    }

@app.get('/users/{user_id}') 
def get_user(user_id : int ) :
    return{
        'user_id' : user_id
    }