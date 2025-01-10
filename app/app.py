from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w aplikacji DevOps!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/about')
def about():
    return "To jest strona 'O nas'."
