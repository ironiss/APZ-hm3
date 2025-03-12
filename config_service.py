from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from config import MESSAGES_SERVICE, LOGGING_SERVICE_PORTS

app = FastAPI()


class AvailableAPI(BaseModel):
    log_s: List[str]
    mes_s: str


@app.get("/all_ports")
def handle() -> AvailableAPI:
    """
    Returns a static text.
    """

    all_appis = {
        "log_s": [f"http://" + "logging_service_" + str(port-5001) + ":" + str(port) for port in LOGGING_SERVICE_PORTS],
        "mes_s": f"http://" + "message_service" + ":" + str(MESSAGES_SERVICE)
    }

    return all_appis

