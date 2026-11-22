from flask import Flask, request
import io
import contextlib

app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    code = request.args.get("code") or request.form.get("code") or request.get_data(as_text=True)
    compiled_code = compile(code, "<string>", "exec")
    output = io.StringIO()

    with contextlib.redirect_stdout(output):
        exec(compiled_code)

    return output.getvalue()
