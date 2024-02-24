from BackEnd import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('WebBegin.html')

@app.route('/post', methods=['POST'])
def post():
    return "recived: {}".format(request.form)

if __name__ == "__main__":
    app.run(debug=True)