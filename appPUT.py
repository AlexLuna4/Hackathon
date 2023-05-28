from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    coment : bool

app = FastAPI()
@app.put("/consulta")
def consulta_model(d:Input):
    if d.coment == True:
        return {'El clima es malo'}