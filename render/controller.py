import requests

RELAY_URL = "https://your-render-service.onrender.com/command"

payload = {
    "command": "run_script",
    "params": {
        "arg1": "hello",
        "arg2": "123"
    }
}

response = requests.post(RELAY_URL, json=payload)
print("✅ Render応答:", response.json())
