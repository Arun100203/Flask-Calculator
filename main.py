from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def result():
    ans = 0
    if request.method == 'POST':
        try:
            ans = eval(str(request.form.get("result")))
        except:
            ans = "Invalid opertaion"

    return render_template('index.html', answer=ans)


if __name__ == "__main__":
    app.run(debug=True)
