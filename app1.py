from google_trans_new import google_translator
import os
from flask import Flask , request ,jsonify
import json
import base64
from flask_cors import CORS


translator = google_translator()

#text to text translation
def translate(text ,output_lang):
    translated_text = translator.translate(text , lang_tgt = output_lang)
    return translated_text

#_______________________________________________________________________________________________
 
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing


@app.route('/voice_translate',methods=['POST'])
def translate_voice_endpoint():
    try:
#         #request data from client
        data = request.get_json()
    
        print("Received data:", data)

        if not data:
            return jsonify({'error':'Missing recognized_text or output_language'}),400
       
        output_language = data['output_language']
        recognized_text = data['recognized_text']
      
    
#        #translate text to text
        translated_text = translate(recognized_text,output_language)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
       print(f'Error: {e}')
       return jsonify({'error': 'Internal Server Error'}), 500
      
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)


