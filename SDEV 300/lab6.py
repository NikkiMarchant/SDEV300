"""Lab6. Nicole Marchant. Website."""
import datetime
from flask import Flask
from flask import render_template
from flask_assets import Environment


app = Flask(__name__)

assets = Environment(app)

@app.route('/')
@app.route('/home')
def main():
    """Main function"""
    return render_template('home.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

@app.route('/types')
def types():
    """Types of Axolots"""
    return render_template('types.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

@app.route('/images')
def images():
    """Images of Axolots"""
    return render_template('images.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

@app.route('/external')
def external():
    """External Links"""
    return render_template('external.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

if __name__ == "__main__":
    app.run(debug=True)
