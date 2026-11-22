from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    code = request.values.get('code', '')
    compiled = compile(code, '<string>', 'exec')
    exec(compiled)
    return "Code executed"
