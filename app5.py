from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def log():
    return render_template('login1.html')

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['username']
    passwrd = request.form['userpass']
    if uname == "godwin" and passwrd == "1234":
        return "Welcome %s" % uname + request.method
    else:
        return "Error in logging in" + request.method
if __name__ == '__main__':
    app.run(debug=True)