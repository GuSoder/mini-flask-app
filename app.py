from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click-me')
def click_me():
    return render_template('index.html', message="🎉 You clicked the button! Welcome to the interactive Flask app!")

@app.route('/about')
def about():
    return render_template('index.html', message="📚 This is a cool Flask app enhanced with HTML styling, CSS, and interactive buttons!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')