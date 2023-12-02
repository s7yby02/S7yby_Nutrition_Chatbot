from fastapi import FastAPI
from pydantic import BaseModel
import json
from model.model import predict_class, get_response
import os

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
async def chat_endpoint(message: Message):
    ints = predict_class(message.text.lower())
    dir_path = os.path.dirname(os.path.realpath(__file__))
    intents = json.loads(open(os.path.join(dir_path, 'model/intents.json')).read())
    response = get_response(ints, intents)
    return {"response": response}