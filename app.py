from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        num_1 = int(request.form.get('num_1'))
        num_2 = int(request.form.get('num_2'))
        return render_template('index.html', ans=num_1 + num_2)

if __name__ == '__main__':
    app.run(debug=True)
