from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests

app = FastAPI()

class UserMessage(BaseModel):
    message: str

RASA_ENDPOINT = "http://localhost:5005/webhooks/rest/webhook"

@app.post("/chat/")
async def chat(user_message: UserMessage):
    response = requests.post(RASA_ENDPOINT, json={"message": user_message.message})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get a response from the chatbot"}

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("templates/index.html") as f:
        return HTMLResponse(content=f.read())
