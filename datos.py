from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def google_graphic():
    # Lee el JSON desde el archivo
    with open('hcorto.json', 'r') as file:
        data = json.load(file)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)