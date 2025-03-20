import flask


@app.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
