from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/experience')
def projects():
    return render_template('experience.html')

@app.route('/contact_me')
def projects():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
