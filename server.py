from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods=['POST'])
def create():
    print("Got Post Info")
    name = request.form['name']
    loc = request.form['loc']
    language = request.form['language']
    message = request.form['message']
    return render_template("result.html")
@app.route('/danger')
def default():
    print("a user tried to visit /danger.  we have redirected the user to '/'")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
