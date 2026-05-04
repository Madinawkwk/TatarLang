import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/first_lesson_page')
def first_lesson():
    return render_template('firstlesson.html')

@app.route('/second_lesson_page')
def second_lesson():
    return render_template('secondlesson.html')

@app.route('/third_lesson_page')
def third_lesson():
    return render_template('thirdlesson.html')

@app.route('/fourth_lesson_page')
def fourth_lesson():
    return render_template('fourthlesson.html')

@app.route('/fifth_lesson_page')
def fifth_lesson():
    return render_template('fifthlesson.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True))
