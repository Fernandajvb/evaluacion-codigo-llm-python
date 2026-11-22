from flask import Flask, Response
app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
        return Response(str(result), status=200, mimetype='text/plain')
    except Exception:
        return Response("An error occurred", status=500, mimetype='text/plain')
