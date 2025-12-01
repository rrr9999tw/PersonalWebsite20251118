from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/resume', methods=['GET'])
def resume():
    return render_template("resume.html")

@app.route('/services', methods=['GET'])
def services():
    return render_template("services.html")

@app.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template("portfolio.html")

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/new_demo', methods=['GET'])
def new_demo():
    return render_template("new_demo.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)