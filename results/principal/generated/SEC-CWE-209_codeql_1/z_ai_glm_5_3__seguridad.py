import logging

from flask import Flask, jsonify

app = Flask(__name__)

# Never enable the interactive debugger in production (it allows remote code
# execution if an exception page is reached).
app.config["DEBUG"] = False

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("server")


def do_computation():
    raise Exception("Secret info")


@app.errorhandler(404)
def not_found(_error):
    return jsonify(error="Not found"), 404


@app.errorhandler(405)
def method_not_allowed(_error):
    return jsonify(error="Method not allowed"), 405


@app.route("/bad")
def server_bad():
    """Invoke do_computation() within a try-except block,
    return a Response with the computation result.
    """
    try:
        result = do_computation()
    except Exception:
        # Log the full traceback server-side only; never send it to the client.
        logger.exception("Computation failed for request to /bad")
        # Generic message: no exception type, message, or stack trace is exposed.
        return (
            jsonify(error="An internal error occurred while processing the request."),
            500,
        )
    return jsonify(result=result), 200


if __name__ == "__main__":
    app.run()
