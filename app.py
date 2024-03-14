# Libraries for users_to_mongo

from scripts.eco_function import send_emails
#----------------------------------------------------------------------
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def echo_function():
    """
    Recibe un JSON a través de un POST request y lo devuelve.

    Retorna:
        dict: El mismo JSON si es válido.
    """
    try:
        data = request.json
        headers = dict(request.headers)
        params = request.args.to_dict()
        
        # Concatenando data, headers y params en una cadena para incluir en el cuerpo del correo
        body_content = f"Data: {data}\nHeaders: {headers}\nParams: {params}"
        
        send_emails('bry3639@gmail.com', 'tzbyrgqfygxmifgd', 'bry3639@gmail.com', str(body_content))
        print(data, 'json enviado')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)