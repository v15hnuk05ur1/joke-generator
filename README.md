# AI-Powered Family-Friendly Joke Generator 🤖😂

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A web application that generates safe, appropriate jokes using Large Language Models (LLMs), with content filtering for all audiences.



![Application Interface](screenshot.png) <!-- Add screenshot -->

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup Instructions](#setup-instructions)
- [API Configuration](#api-configuration)
- [Deployment](#deployment)
- [Safety Measures](#safety-measures)
- [Contributing](#contributing)
- [License](#license)

## Features ✨
- 🧠 LLM-powered joke generation (Google Gemini)
- 👨👩👧👦 Strict content filtering system
- 📱 Responsive web interface
- ⏳ Interactive loading states
- 🛠️ Comprehensive error handling
- 🔐 Secure environment management

## Technology Stack 🛠️
- **Backend Framework**: Python Flask
- **AI Engine**: Google Gemini API
- **Frontend**: Vanilla JS + CSS3
- **Security**: Dotenv configuration
- **Packaging**: pip/PyPI

## Setup Instructions 📦

### Prerequisites
- Python 3.10+
- Google Gemini API key
- pip package manager

 ### API Configuration 🔑

    1.Obtain API key from Google AI Studio
    2.Create .env file in project root:

    GEMINI_API_KEY=your_actual_key_here

Running the Application 🚀
    
    python app.py

Access via: http://localhost:5000

Deployment ☁️
Supported platforms:

    Render: Python Web Service

    PythonAnywhere: Flask configuration

    Heroku: Add Procfile with Gunicorn

Ensure environment variables are configured in your hosting platform.
Safety Measures 🔒

Multi-layer content protection:

    Explicit prompt engineering

    Model-level safety filters

    Client-side validation

    Server-side content checks

    Rate limiting (client-side)
### Installation
```bash
# Clone repository
git clone https://github.com/your-username/joke-generator.git
cd joke-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt



