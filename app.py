from flask import Flask, render_template
app = Flask(__name__, static_folder='./templates/images')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mondai-1')
def question_1():
    return render_template('question1.html')

if __name__ == "__main__":
    app.run()