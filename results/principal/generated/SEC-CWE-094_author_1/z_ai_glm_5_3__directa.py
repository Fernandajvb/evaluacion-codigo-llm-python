from flask import Flask, request

app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    code = request.args.get("code", "")
    if not code:
        return "No code provided", 400

    compiled_code = compile(code, "<evalcode>", "exec")
    exec(compiled_code, {})
    return "Code executed"

if __name__ == "__main__":
    app.run()
