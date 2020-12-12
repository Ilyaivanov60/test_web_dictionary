from flask import Flask, render_template, redirect, url_for, request
from get_translation import get_translate

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('eng'):
        word = request.args.get('eng')
        translate_word = get_translate(word)
        return render_template('index.html', translate_word=translate_word)
    else:
        translate_word = 'не правильный аргумент'
        return render_template('index.html', translate_word=translate_word)

# @app.route('/add_word')
# def add_word():
#     return redirect(url_for('/'))

if __name__ == "__main__":
    app.run(debug=True)
