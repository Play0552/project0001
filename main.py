from flask import Flask, url_for, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd7h6dfg786hgf56dhfg6d85h98'

catigories = ['чайники', 'хуяйники', 'и так далее']

@app.route('/')
def index():
    return render_template('index.html', catigories=catigories)

if __name__ == '__main__':
    app.run(debug=True)

