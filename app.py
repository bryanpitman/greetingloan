from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    html = "<html><body><h1>Welcome</h1><body></html>"
    return html

@app.get('/welcome/home')
def say_welcome_home():
    html = "<html><body><h1>Welcome Home</h1><body></html>"
    return html

@app.get('/welcome/back')
def say_welcome_back():
    html = "<html><body><h1>Welcome Back</h1><body></html>"
    return html