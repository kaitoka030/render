from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute',methods=['POST'])
def execute():
    data = request.get_json()
    print("💻 実行指令:", data)

    command = data.get("command")
    parmars = data.get("parmars",{})

    if command == "run_script":
        #引数の組み立て
        args = []
        for key,value in parmars.items():
            args.append(str(value))

        # 例: python3 script.py hello 123
        result = subprocess.run(
            ["python3", "script.py"] + args,
            capture_output=True,
            text=True
        )
        return jsonify({
            "status": "ok",
            "stdout": result.stdout,
            "stderr": result.stderr
        })
    
    else:
        return jsonify({"error": "Unknown command"}), 400

if __name__ == '__main__':
    app.run(port=5000)