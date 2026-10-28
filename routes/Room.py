from flask import Blueprint, request, jsonify

from service import RoomDao

rooms_bp = Blueprint("rooms", __name__)

@rooms_bp.route("/rooms", methods=["PUT"])
def create_room():
    try:
        files = request.json['files']
        client_id = request.json['clientId']

        room_id = RoomDao.create_room(client_id)
        RoomDao.add_files_to_room(room_id, files)

        return jsonify(
            roomId = room_id
        )
    except Exception as ex:
        return jsonify(
            message = "Something went wrong",
            error = ex.args
        ), 500