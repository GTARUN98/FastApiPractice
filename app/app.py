from fastapi import FastAPI
app = FastAPI()

todos = [
    {"id": "1",
    "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]

@app.get("/",tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}


#Get --> Read Todo
@app.get('/todo',tags=['todos'])
async def get_todo() -> dict:
    return {"data" : todos}

#Post -->Create Todo
@app.post('/todo',tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data": "A todo has been added successfully"
    }
#Put --> Update Todo

@app.put("/todo/{id}",tags=['todos'])
async def update_todo(id: int , body: dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity'] = body['Activity']
            return{
                "data":"todo with id no as {id} is updated"
            }
    return{
        "data":"todo with the id no is not found"
    }
#Delete -->Delete Todo

@app.delete("/todo/{id}",tags=['todos'])
async def delete_todo(id:int) ->dict:
    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
            return {
                "data" : "The todos of id {id} is removed successfully"
            }
    return {
        "data" : "The todos is not found"
    }


