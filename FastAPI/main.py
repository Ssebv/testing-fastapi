from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"nombre" : "pepe"}

@app.get('/url')
async def url():
    return {"url": "http://localhost"}


# * Para correr el servidor de desarrollo
# uvicorn main:app --reload

# * Para ver la documentación
# http://localhost:8000/docs
# http://localhost:8000/redoc