from flask import Flask, Response
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
        return Response(str(result), mimetype='text/plain')
    except Exception:
        return Response(traceback.format_exc(), mimetype='text/plain')
