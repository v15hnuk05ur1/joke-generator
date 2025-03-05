from flask import Flask, render_template, jsonify, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def generate_safe_joke():
    prompt = """Generate a family-friendly joke that is:
    - Appropriate for all ages
    - Free of any offensive, dark, or NSFW content
    - Culturally sensitive
    - Focused on wordplay or harmless situations"""
    
    response = model.generate_content(prompt)
    return response.text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_joke():
    try:
        joke = generate_safe_joke()
        return jsonify({'joke': joke, 'error': None})
    except Exception as e:
        return jsonify({'joke': None, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=False)
