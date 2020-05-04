from flask import Flask, render_template

app = Flask(__name__) # kind like a place holder for the current module

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__': # that means that it is the script that's going to be executed
    app.run(debug=True)
 