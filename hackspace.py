from flask import Flask, request, render_template

import facebook,vk,telegram,instagram

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=1024)
