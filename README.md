# PublicBenefit ChatBot

A lightweight Flask-based chatbot connected to OpenAI’s API, designed as a foundational tool for the Canadian charitable sector.  
This project is the starting point for a future Retrieval-Augmented Generation (RAG) system and private organizational bots.

## Features

- Chatbot web interface powered by OpenAI GPT models
- Flask-based lightweight backend
- Secure API key management via environment variables
- Local chat logging to `chatlog.log`
- Viewable logs through `/logs` route
- Simple, responsive web UI

## Technology Stack

- **Python 3.10+**
- **Flask 2.3+**
- **OpenAI Python API 1.13+**
- **Gunicorn** (for production WSGI server)

## Project Structure

publicbenefit-chatbot/
├── publicbenefit-chatbot.py
├── requirements.txt
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── logs.html
├── static/
│   └── style.css
├── start-chatbot.bat
├── stop-chatbot.bat
├── README.md


## How to Run Locally

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Set your OpenAI API key in a `.env` file:

    ```bash
    OPENAI_API_KEY=your-openai-key-here
    ```

3. Start the chatbot server:

    ```bash
    python publicbenefit-chatbot.py
    ```

4. Visit [http://localhost:5000/](http://localhost:5000/) in your web browser.

## Deployment

This project is ready for public deployment using Render.com, Railway.app, or other Python-compatible hosting services.

Production deployment uses:

```bash
gunicorn publicbenefit-chatbot:app


## Deployment

This project is ready for public deployment using Render.com, Railway.app, or other Python-compatible hosting services.

Production deployment uses:

    gunicorn publicbenefit-chatbot:app

## Roadmap

- Add BART functionality (summarization, rewriting, translation)
- Add RAG functionality (document retrieval and knowledge augmentation)
- User authentication and permission tiers
- Full UI/UX refresh for public users
- Multi-language support

## License

_TBD – License will be added at a later stage._

## Credits

Developed by Paul B. Wolfe with guidance and support from the PublicBenefit development initiative.  
Built with ❤️ for the charitable sector.
