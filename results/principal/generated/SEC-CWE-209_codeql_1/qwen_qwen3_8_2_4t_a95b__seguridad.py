from flask import Flask, Response

app = Flask(__name__)
app.config["DEBUG"] = False

def do_computation():
    raise Exception("Computation failed")

@app.route("/bad", methods=["GET"])
def server_bad():
    try:
        result = do_computation()
    except Exception:
        app.logger.error("Computation failed")
        return Response("Internal Server Error", status=500, mimetype="text/plain")
    return Response(str(result), mimetype="text/plain")
