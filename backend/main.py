from fastapi import FastAPI
from pydantic import BaseModel

from backend.pipeline import process_ticket

app = FastAPI()
    

class TicketRequest(BaseModel):
    ticket: str


@app.get("/")
def home():
    return {"message": "Customer Support AI is running"}


@app.post("/predict")
def predict(request: TicketRequest):

    result = process_ticket(request.ticket)

    return result