from flask import Flask, request, jsonify
import fitz  # PyMuPDF

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    # Check if the 'pdf' file is in the request
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Read the file's bytes directly
        file_bytes = file.read()
        # Open the PDF from the in-memory byte stream
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        
        # Extract text from each page
        extracted_text = ""
        for page in doc:
            extracted_text += page.get_text() + "\n"
            
        return jsonify({'notes': extracted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
