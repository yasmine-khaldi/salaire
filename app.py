from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')
@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

if __name__ == '__main__':
    app.run(debug=True)
