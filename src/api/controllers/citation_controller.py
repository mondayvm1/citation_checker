import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import logging
import traceback

from flask import request, jsonify
from flask_restful import Resource
from werkzeug.utils import secure_filename
import os
# from ..services.citation_service import CitationService

from services.citation_service import CitationService

class PdfCitationResource(Resource):
    def __init__(self):
        self.citation_service = CitationService()

    def post(self):
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join("/tmp", filename)
            file.save(file_path)

            try:
                extracted_text = self.citation_service.extract_text_from_pdf(file_path)
                result = self.citation_service.check_citation(extracted_text)

                os.remove(file_path)

                return {"message": "Citation checked", "result": result}, 200
            except Exception as e:
                print("Error occurred:")
                print(traceback.format_exc())  # Print the traceback to the terminal
                return {"error": "Failed to process file"}, 500
        else:
            return {"error": "Unsupported file format"}, 400

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

