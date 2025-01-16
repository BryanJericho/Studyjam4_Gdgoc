from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return "About Page"


//http handling request
from flask import Flask, request, jsonify

app = Flask(__name__)

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
    app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

//templating
# Route untuk halaman Home
@app.route('/')
def home():
    return render_template('home.html', title="Home Page")

# Route untuk halaman About
@app.route('/about')
def about():
    return render_template('about.html', title="About Page")

if __name__ == '__main__':
    app.run(debug=True)
