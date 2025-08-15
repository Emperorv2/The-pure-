import json

def save_to_json(user_id: int, text: str):
    data = {"user_id": user_id, "text": text}
    with open("temp_logs.json", "a") as f:
        f.write(json.dumps(data) + "\n")