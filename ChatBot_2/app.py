from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load JSON data from multiple files
def load_multiple_medicine_data():
    file_paths = ['templates/json/medicines1.json']
    medicines = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
            medicines.extend(data)
    return medicines

# Find medicine information based on name
def find_medicine_info(medicine_name, medicines):
    for medicine in medicines:
        # Check if the name contains the user input (case-insensitive)
        if medicine_name.lower() in medicine["generic_name"].lower():
            return f'generic_name: {medicine["generic_name"]}\nStrength: {medicine["strength"]}\nComposition: {medicine["composition"]}\nCompany: {medicine["company"]}\nMore Info: {medicine["product_info_url"]}'
    return "Sorry, I couldn't find that medicine."

# Load medicines data once at startup
medicines = load_multiple_medicine_data()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    response = find_medicine_info(user_input, medicines)
    return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)
