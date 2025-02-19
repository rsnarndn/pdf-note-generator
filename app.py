from flask import Flask, request, jsonify
from io import BytesIO
from pdfminer.high_level import extract_text

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask server is running!"

@app.route('/upload', methods=['POST'])
def upload_pdf():
    # Verify that a file is provided in the request
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Read the PDF file into an in-memory stream
        file_stream = BytesIO(file.read())
        # Extract text from the PDF using pdfminer.six
        extracted_text = extract_text(file_stream)
        
        # Optionally, generate a summary using your summarization module:
        # from summarizer import generate_summary
        # summary = generate_summary(extracted_text)
        # For now, we'll return the extracted text for testing:
        return jsonify({'notes': extracted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)






