import uuid
import os

from flask import jsonify, request, Blueprint

from service import FileDao, ClientFilesDao
from storage import AzureUpload
from utils import FileUtil, ShortUrlUtil

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 20 * 1024 * 1024

files_bp = Blueprint('files', __name__)

@files_bp.route("/files/upload", methods=["POST"])
def files_upload():
    try:
        client_id = request.args.get("clientId")

        if client_id is None:
            return jsonify(
                message = "ClientId is not provided"
            )

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

        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)

        if file_size > MAX_FILE_SIZE:
            return jsonify(
                message = f"File too large, max value accepted is {MAX_FILE_SIZE / 1024 / 1024}mb"
            )

        file_id = str(uuid.uuid4())
        filename = f"{file_id}.{extension}"

        long_url = AzureUpload.upload_file_to_azure(filename, file)
        url = ShortUrlUtil.shorten_url(long_url)

        FileDao.insert_file(file_id, filename, file_size, extension, url)
        ClientFilesDao.insert_file_for_client(client_id, file_id)

        return jsonify(
            fileUrl = f"{url}"
        )
    except Exception as ex:
        return jsonify(
            message = "Something went wrong",
            error = ex.args
        ), 500