from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

def check_strength(password):
    if len(password) < 6:
        return {"message": "Too weak", "class": "text-red-500"}
    elif len(password) < 10:
        return {"message": "Medium strength", "class": "text-yellow-500"}
    else:
        return {"message": "Strong password", "class": "text-green-500"}

@app.route('/check', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    return jsonify(check_strength(password))

@app.route('/generate', methods=['GET'])
def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(12))
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)