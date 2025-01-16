from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'ini adalah halaman utama'

# Handling GET request
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a GET request"})

# Handling POST request
@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({"message": "This is a POST request", "data_received": data})

# Handling PUT request
@app.route('/data/<int:id>', methods=['PUT'])
def put_data(id):
    data = request.json
    return jsonify({"message": f"Data with ID {id} updated", "updated_data": data})

# Handling DELETE request
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    return jsonify({"message": f"Data with ID {id} deleted"})

if __name__ == '__main__':
    app.run(debug=True,port=8080), 
