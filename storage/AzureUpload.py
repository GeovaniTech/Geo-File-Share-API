import os

from azure.storage.blob import BlobServiceClient


def get_blob_service_client():
    try:
        connect_str = str(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))

        return BlobServiceClient.from_connection_string(connect_str)
    except Exception as ex:
        print('Exception:')
        print(ex)


def upload_file_to_azure(filename, file):
    try:
        container = str(os.getenv("AZURE_STORAGE_CONTAINER"))
        blob_service_client = get_blob_service_client()

        blob_client = blob_service_client.get_blob_client(container=container, blob=filename)
        file_url = blob_client.upload_blob(file, overwrite=True)

        # TODO - Save metadata on DB.

        return file_url
    except Exception as ex:
        print('Exception:')
        print(ex)

