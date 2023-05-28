from fastapi import FastAPI

app = FastAPI()

@app.get("/consulta")
def consulta_app(coment: str):
    #if the ICA is bad, alert with a messagge
    coment = True
    if coment == True:
        return{'El clima es malo': 1}
    else:
        return{'No pasa nada': 0}