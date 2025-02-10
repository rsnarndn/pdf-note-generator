from flask import Flask, request, jsonify
import fitz  # PyMuPDF
from Summarizer import generate_summary  # Ensure this function is defined in Summarizer.py

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    # Verify that a file is provided in the request
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Read the PDF file as bytes from the in-memory stream
        file_bytes = file.read()
        # Open the PDF using PyMuPDF from the in-memory data
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        
        # Extract text from each page of the PDF
        extracted_text = ""
        for page in doc:
            extracted_text += page.get_text() + "\n"
        
        # Generate a summary using your local summarization module
        summary = generate_summary(extracted_text)
        
        # Return the summary as a JSON response
        return jsonify({'notes': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

