import openai
import os
import logging
from flask import Flask, render_template, request

app = Flask(__name__)

# Set your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Logging configuration
logging.basicConfig(
    filename='chatlog.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Main chatbot route
@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        logging.info(f"User prompt: {prompt}")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            answer = response.choices[0].message["content"].strip()
            logging.info(f"Chatbot response: {answer}")
            return render_template('index.html', response=answer)

        except Exception as e:
            error_message = f"Error: {str(e)}"
            logging.error(error_message)
            return render_template('index.html', response=error_message)

    return render_template('index.html', response=None)

# Route to view chat logs
@app.route('/logs')
def view_logs():
    try:
        with open('chatlog.log', 'r') as f:
            log_content = f.read()
    except FileNotFoundError:
        log_content = "No logs found."

    return render_template('logs.html', logs=log_content)

# Run the Flask app locally
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
