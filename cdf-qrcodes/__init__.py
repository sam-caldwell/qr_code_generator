
import azure.functions as func
import io
import logging
import mimetypes
import pyqrcode


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = req.params.get('url',"not_set")
        id = req.params.get('id',"not_set")

        mime_type = "image/png"

        file_name=f"{id}.png"

        headers={
            "content-type":mime_type,
            "content-disposition":f"'attachment; filename=\"{file_name}\"'"
        }

        qr_code = pyqrcode.create(f"{url}?id={id}")
        buffer = io.BytesIO()
        qr_code.png(buffer)
        resp = func.HttpResponse(buffer.getvalue(),headers=headers, mimetype=mime_type)
        return resp
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"An error has occured.  Check your inputs.")
