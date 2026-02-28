from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# home page route/location
@app.route('/')
def index():
    return render_template('index.html')

# about page route/location
@app.route('/about')
def about():
    return render_template('about.html')

# networking concepts page route/location
@app.route('/networking')
def networking():
    return render_template('networking.html')

#run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)