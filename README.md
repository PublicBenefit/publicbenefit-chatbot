# PublicBenefit ChatBot

A lightweight, AI-powered chatbot built with Flask and connected to OpenAI’s API — designed to support Canadian charities with compliance, operations, and knowledge delivery.

This chatbot is the first deployed component of a larger system aimed at enabling one human to manage hundreds of charities efficiently — by exception, not by task.

## 🔍 Purpose

The PublicBenefit ChatBot serves as an interface for retrieving structured, reliable answers based on CRA guidance and internal knowledge structures (starting with the T3010). It’s designed to grow into a Retrieval-Augmented Generation (RAG) system powered by live data and domain-specific knowledge agents.

## ✨ Features

- Chat interface powered by OpenAI GPT models
- Flask-based lightweight backend
- Secure API key management via `.env` file
- Local chat logging to `chatlog.log`
- Web-based log viewer at `/logs`
- Simple, responsive HTML/CSS UI

## 🧱 Technology Stack

- **Python 3.10+**
- **Flask 2.3+**
- **OpenAI Python API 1.13+**
- **Gunicorn** for production WSGI serving
- **Render.com** for public deployment

## Project Structure

publicbenefit-chatbot/
├── publicbenefit-chatbot.py     # Main Flask app
├── requirements.txt             # Dependencies
├── .gitignore
├── .env                         # API key (excluded from Git)
├── templates/                   # HTML templates
│   ├── base.html
│   ├── index.html
│   └── logs.html
├── static/                      # CSS and frontend assets
│   └── style.css
├── start-chatbot.bat            # Windows start script
├── stop-chatbot.bat             # Windows stop script
├── chatlog.log                  # Local chat history (rotating)
└── README.md                    # This file


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
