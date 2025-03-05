from flask import Flask, render_template, jsonify, request
import os
import llama  # make sure to install the appropriate Llama client package

app = Flask(__name__)

# Configure Llama
api_key = os.getenv("LLAMA_API_KEY")
if not api_key:
    raise ValueError("No API_KEY found. Please set the LLAMA_API_KEY environment variable.")
llama.configure(api_key=api_key)

# (Optional) List available models if supported by the Llama client
# models = llama.list_models()
# print("Available models:", models)

# Use a valid model from Llama - replace 'llama-1' with the actual model if needed
model = llama.ChatModel('llama-1')

def generate_safe_joke():
    prompt = """Generate a family-friendly joke that is:
    - Appropriate for all ages
    - Free of any offensive, dark, or NSFW content
    - Culturally sensitive
    - Focused on wordplay or harmless situations"""
    
    response = model.generate(prompt)  # Adjust this call per Llama API docs
    return response["text"]

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
