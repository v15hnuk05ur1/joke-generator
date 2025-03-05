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
