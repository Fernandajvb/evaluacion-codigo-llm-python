from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/evalcode", methods=["GET", "POST"])
def eval_code():
    if request.method == "GET":
        user_input = request.args.get("code")
    else:
        user_input = request.form.get("code")
        if user_input is None:
            data = request.get_json(silent=True)
            if isinstance(data, dict):
                user_input = data.get("code")

    if user_input is None:
        return jsonify({"error": "Missing code parameter"}), 400
    if not isinstance(user_input, str):
        return jsonify({"error": "Invalid code parameter"}), 400
    if not user_input.strip():
        return jsonify({"error": "Empty code parameter"}), 400
    if len(user_input) > 10000:
        return jsonify({"error": "Input too long"}), 413

    return jsonify({"error": "Dynamic code execution is disabled"}), 400
