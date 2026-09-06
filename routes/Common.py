from flask import jsonify, Blueprint

commons_bp = Blueprint("common", __name__)


@commons_bp.route("/test", methods=["GET", "POST"])
def test_endpoint():
    return jsonify(
        message = "Hello, world!"
    ), 200