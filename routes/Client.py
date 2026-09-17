from flask import jsonify, request, Blueprint
from service import ClientDao, PlanDao

clients_bp = Blueprint('clients_bp', __name__, url_prefix='/clients')

@clients_bp.route('/clients', methods=['PUT'])
def insert_client():
    try:
        client_id = request.json['clientId']

        ClientDao.insert_client(client_id)

        return jsonify(
            message = f"Client {client_id} has been created"
        ), 201
    except Exception as ex:
        print(ex)
        return jsonify(
            error = ex.args
        ), 500


@clients_bp.route('/clients', methods=['PATCH'])
def update_client_plan():
    try:
        client_id = request.json['clientId']
        plan_id = request.json['planId']

        ClientDao.update_client_plan(client_id, plan_id)

        return jsonify(
            message = f"Client {client_id} has been updated"
        ), 200
    except Exception as ex:
        return jsonify(
            message = ex.args
        )