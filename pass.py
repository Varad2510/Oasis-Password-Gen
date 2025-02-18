from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

# Function to generate a random password
def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/generate-password', methods=['GET'])
def password_generator():
    try:
        length = int(request.args.get('length', 12))  # Default length is 12
        use_upper = request.args.get('use_upper', 'true').lower() == 'true'
        use_lower = request.args.get('use_lower', 'true').lower() == 'true'
        use_numbers = request.args.get('use_numbers', 'true').lower() == 'true'
        use_symbols = request.args.get('use_symbols', 'false').lower() == 'true'

        password = generate_password(length, use_upper, use_lower, use_numbers, use_symbols)

        return jsonify({"password": password})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
