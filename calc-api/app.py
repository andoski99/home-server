from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    result = a + b
    return jsonify({'a': a, 'b': b, 'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)