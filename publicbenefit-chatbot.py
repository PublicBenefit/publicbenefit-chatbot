import openai
import os
import logging
from flask import Flask, render_template, request, send_file
from logging.handlers import RotatingFileHandler

# Ensure log file exists
if not os.path.exists('chatlog.log'):
    open('chatlog.log', 'w').close()

# Setup logging with rotation: 100 KB max, keep 3 old logs
handler = RotatingFileHandler('chatlog.log', maxBytes=100_000, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Flask app initialization
app = Flask(__name__)

# OpenAI API key setup
openai.api_key = os.getenv("OPENAI_API_KEY")

# Main chatbot route
@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        logging.info(f"User prompt: {prompt}")

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            answer = response.choices[0].message.content.strip()
            logging.info(f"Chatbot response: {answer}")
            return render_template('index.html', response=answer)
        except Exception as e:
            error_message = f"Error: {str(e)}"
            logging.error(error_message)
            return render_template('index.html', response=error_message)

    return render_template('index.html', response=None)

# View chat logs route
@app.route('/logs')
def view_logs():
    try:
        with open('chatlog.log', 'r') as f:
            log_content = f.read()
    except FileNotFoundError:
        log_content = "No logs found."

    return render_template('logs.html', logs=log_content)

# Download log file
@app.route('/download-log')
def download_log():
    return send_file('chatlog.log', as_attachment=True, download_name='chatlog.txt')

# Run Flask app locally
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
