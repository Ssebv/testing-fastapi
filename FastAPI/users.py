from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id : int
    name: str
    email: str
    password: str

users_list = [
    User(id= 1,name="pepe", email="email", password="password"),
    User(id= 2,name="pepe1", email="email1", password="password1"),
    User(id= 3,name="pepe2", email="email2", password="password2"),
    User(id= 4,name="pepe3", email="email3", password="password3")
]
# my_second_user= {"id": 5,"name":"pepe4", "email":"email4", "password":"password4"}
# my_second_user : User = User(**my_second_user)

@app.get('/users/')
async def users():
    return users_list



# * Path parameters
@app.get('/users/{id}/')
async def user(id: int):
    return search_user(id)

# * Query parameters
@app.get('/user/') # http://localhost:8000/user/?id=1
async def userquery():
    return users_list

@app.post('/user/')
async def create_user(user: User):
    return create_user(user)

@app.put('/user/')
async def update_user(user: User):
    return update_user2(user)

@app.delete('/user/{id}')
async def delete_user(id: int):
    return delete_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "User not found"}

def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "User already exists"}
    else:
        users_list.append(user)
        return user

def update_user(user: User):
    if type(search_user(user.id)) == User:
        users_list[user.id - 1] = user
        return user
    else:
        return {"error": "User not found"}
    
def update_user2(user: User):
    if type(search_user(user.id)) == User:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == user.id:
                users_list[index] = user
                return user
    else:
        return {"error": "User not found"}

def delete_user(id: int):
    if type(search_user(id)) == User:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == id:
                users_list.pop(index)
                return {"message": "User deleted"}
    else:
        return {"error": "User not found"}