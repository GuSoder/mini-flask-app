from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action1')
def action1():
    return "You clicked Action 1!"

@app.route('/action2')
def action2():
    return "You clicked Action 2!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')