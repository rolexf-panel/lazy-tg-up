import requests
from config import PIXELDRAIN_API

def upload(path):
    with open(path, "rb") as f:
        r = requests.post(
            "https://pixeldrain.com/api/file",
            headers={"Authorization": f"Bearer {PIXELDRAIN_API}"},
            files={"file": f},
            timeout=600
        )
    r.raise_for_status()
    return "https://pixeldrain.com/u/" + r.json()["id"]
