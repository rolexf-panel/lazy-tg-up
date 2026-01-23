import requests

def upload(path):
    server = requests.get("https://api.gofile.io/servers").json()["data"]["servers"][0]["name"]
    with open(path, "rb") as f:
        r = requests.post(
            f"https://{server}.gofile.io/contents/uploadfile",
            files={"file": f},
            timeout=600
        )
    data = r.json()
    if data["status"] == "ok":
        return data["data"]["downloadPage"]
