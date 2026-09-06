from flask import jsonify, request, Blueprint
from service import ClientDao

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
            message = "Something went wrong. Please try again.",
            error = ex
        ), 500