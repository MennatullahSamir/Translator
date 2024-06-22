# from google_trans_new import google_translator
import os
from flask import Flask , request ,jsonify
import json
import base64
from flask_cors import CORS
from googletrans import Translator
# from werkzeug.utils import secure_filename
# import pytesseract as pyt
# import cv2

translator = Translator()
# pyt.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"




#text to text translation
def translate(text, output_lang):
    try:
        translated_text = translator.translate(text, dest = output_lang)
        return translated_text.text
    except Exception as e:
        print(f"Error in translation: {e}")
        return None

#_______________________________________________________________________________________________
 
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing
# app.config['UPLOAD_FOLDER'] = 'uploads/'
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400
    
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
    
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     file.save(file_path)
    
#     try:
#         img = cv2.imread(file_path)
#         if img is None:
#             return jsonify({'error': 'Failed to read the uploaded image'}), 500
        
#         extracted_text = pyt.image_to_string(img)
#         translated = translator.translate(extracted_text, dest='ar')
        
#         return jsonify({
#             'extracted_text': extracted_text,
#             'translated_text': translated.text
#         }), 200
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
@app.route('/test', methods=['GET'])
def test_endpoint():
    return jsonify({'message': 'GET request successful'})

@app.route('/voice_translate',methods=['POST'])
def translate_voice_endpoint():
    try:
        #request data from client
        data = request.get_json()
        print("Received data:", data)
        if not data:
            return jsonify({'error':'Missing recognized_text or output_language'}),400
       
        if 'output_language' not in data or 'recognized_text' not in data:
            return jsonify({'error': 'Missing recognized_text or output_language'}), 400
        output_language = data['output_language']
        recognized_text = data['recognized_text']
      
    
        #translate text to text
        translated_text = translate(recognized_text,output_language)
        if translated_text is None:
            return jsonify({'error': 'Translation failed'}), 500
        
        return jsonify({'translated_text': translated_text})
    except Exception as e:
       print(f'Error: {e}')
       return jsonify({'error': 'Internal Server Error'}), 500
      
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)


