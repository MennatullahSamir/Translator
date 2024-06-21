from google_trans_new import google_translator
import os
from flask import Flask , request ,jsonify
import json
import base64
from flask_cors import CORS


translator = google_translator()

#text to text translation
def translate(text, output_lang):
    try:
        translated_text = translator.translate(text, lang_tgt=output_lang)
        return translated_text
    except Exception as e:
        print(f"Error in translation: {e}")
        return None
print(translate("how are you","ar"))
#_______________________________________________________________________________________________
 
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

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


