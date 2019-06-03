from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    forward_message = "Pls click..."
    return render_template('index.html', message=forward_message)

@app.route("/on", methods=['POST'])
def on():
    print(request.args)
    #Moving forward code
    message = "on"
    return render_template('index.html', message=message)
@app.route("/off", methods=['POST'])
def off():
    message = "off"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
