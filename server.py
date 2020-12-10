from flask import Flask
from get_translation import get_translate

app = Flask(__name__)

@app.route('/')
def index():
    return get_translate()

if __name__ == "__main__":
    app.run(debug=True)