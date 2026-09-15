from flask import jsonify, request, Blueprint

from service import PlanDao

plans_bp = Blueprint("plans", __name__)

@plans_bp.route("/plans/plan", methods=["PUT", "PATCH"])
def upsert_plan():
    try:
        plan_id = request.json["id"]
        title = request.json["title"]
        parameters = request.json["parameters"]
        price = request.json["price"]
        currency = request.json["currency"]
        is_active = request.json["isActive"]

        operation = PlanDao.upsert_plan(plan_id, title, parameters, price, currency, is_active)

        if operation == "CREATE":
            return jsonify({"plan_id": plan_id}), 201
        elif operation == "UPDATE":
            return jsonify({"plan_id": plan_id}), 200
    except Exception as ex:
        return jsonify(
            message = ex.args
        ), 500
