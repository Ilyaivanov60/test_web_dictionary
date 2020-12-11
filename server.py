from flask import Flask, render_template
from get_translation import get_translate

app = Flask(__name__)


@app.route('/')
def index():
    translate_word = get_translate('cat')
    return render_template('index.html', translate_word=translate_word)


# @app.route('/second_page')
# def second_page():
#     return 'second_page'

if __name__ == "__main__":
    app.run(debug=True)
