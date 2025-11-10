from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

#envファイル読み込み
load_dotenv()

app = Flask(__name__)

#環境変数からURLを取得
TARGET_PC_URL = os.getenv("TARGET_PC_URL")

@app.route('/',methods=['POST'])
def home():
    return "Render Relay Server ✅"


#操作PCから指令を受け取る
@app.route ('/command',methods=['POST'])
def receive_command():
    try:
        data = request.get_json()
        print(f"操作PCからの受信:{data}")
        if not TARGET_PC_URL:
            return jsonify({"error": "TARGET_PC_URL not set"}), 500
        
        # 別PCへ転送
        response = requests.post(f"{TARGET_PC_URL}/execute", json=data, timeout=10)

        return jsonify({
            "status": "forwarded",
            "target_response": response.json() if response.content else {}
        })
    
    except Exception as e:
        print(f"error:{e}")
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)