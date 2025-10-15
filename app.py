from flask import Flask, request, jsonify, render_template
from llm_analyzer import analyze_code
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main dashboard page."""
    return render_template('index.html')

@app.route('/review', methods=['POST'])
def review_code():
    """API endpoint to receive a code file and return a review."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    if file:
        try:
            # Read the file content
            code_content = file.read().decode('utf-8')
            
            # Get the analysis from the LLM
            review_report = analyze_code(code_content)
            
            return jsonify({"filename": file.filename, "report": review_report})
            
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)