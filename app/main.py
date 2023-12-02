from fastapi import FastAPI
from pydantic import BaseModel
import json
from model.model import predict_class, get_response

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
async def chat_endpoint(message: Message):
    ints = predict_class(message.text)
    intents = json.loads(open('app\model\intents.json').read())
    response = get_response(ints, intents)
    return {"response": response}