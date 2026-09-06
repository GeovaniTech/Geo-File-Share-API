import uuid

from flask import jsonify, request, Blueprint

from storage import AzureUpload
from utils import FileUtil

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

files_bp = Blueprint('files', __name__)

@files_bp.route("/files/upload", methods=["POST"])
def files_upload():
    try:
        if 'file' not in request.files:
            return jsonify(
                message = "No file part"
            ), 400

        file = request.files['file']
        extension = FileUtil.extract_file_extension(file.filename)

        if extension not in ALLOWED_EXTENSIONS:
            return jsonify(
                message = "File extension not allowed"
            ), 400

        file_id = uuid.uuid4()
        filename = f"{file_id}.{extension}"

        url = AzureUpload.upload_file_to_azure(filename, file)

        return jsonify(
            fileUrl = f"{url}"
        )
    except Exception as ex:
        return jsonify(
            message = "Something went wrong",
            error = ex
        ), 500