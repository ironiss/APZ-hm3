from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MessageFedaultHandler(BaseModel):
    static_text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/message_handler")
def handle() -> MessageFedaultHandler:
    """
    Returns a static text.
    """
    return {"static_text": "Not implemented yet"}

