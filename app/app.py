from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w aplikacji DevOps!"

@app.route('/about')
def about():
    return "To jest strona 'O nas'."

@app.route('/data', methods=['GET'])
def get_data():
    return "Oto dane!"

@app.route('/data', methods=['POST'])
def post_data():
    return "Dane zostały zapisane!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

