# URL Shortener

A simple URL shortener web application built with Python Flask for the backend and HTML/CSS/JavaScript for the frontend.

## 🚀 Features

- Shorten long URLs into short, easy-to-share links.
- Redirect short URLs back to the original URLs.
- Clean and simple user interface.
- Copy shortened URL to clipboard with one click.
- Ready to deploy on Render.

## ⚙️ Installation (Local Setup)

### Clone the repository

```bash
git clone https://github.com/aps4934/url-shortener.git
cd url-shortener
```

### Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask app

```bash
python app.py
```

Open your browser at 👉 http://localhost:5000

## 🌐 Deployment on Render

1. Push your code to GitHub (make sure requirements.txt is included).
2. On Render, create a New Web Service and connect this repo.
3. Use the following settings:

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
gunicorn app:app
```

Deploy! 🎉 Your app will be live at `https://<your-app-name>.onrender.com`

## 📂 Project Structure

```
url-shortener/
│
├── app.py               # Flask backend application
├── requirements.txt     # Python dependencies
│
├── templates/           # HTML templates
│   └── index.html
│
└── static/              # Frontend static files
    ├── styles.css
    └── script.js
```

## 👤 Creator

Created by Aditya Pratap Singh.
Feel free to open issues or submit pull requests for improvements!

## 📜 License

This project is licensed under the MIT License.
