"""Lab7. Nicole Marchant. Website."""
import datetime
import re
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import session
from flask_assets import Environment
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.secret_key = 'hv845jg87JaJf084j908jGTHJ0A9uth8043jt9j'

assets = Environment(app)

@app.route('/')
@app.route('/home')
def main():
    """Main function"""
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template('home.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

@app.route('/types')
def types():
    """Types of Axolots"""
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template('types.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

@app.route('/images')
def images():
    """Images of Axolots"""
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template('images.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

@app.route('/external')
def external():
    """External Links"""
    if not session.get('username'):
        return redirect(url_for('login'))
    return render_template('external.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""

    if request.method == 'POST':
        login_user = request.form['username']
        login_pass = request.form['password']
        try:
            with open('passfile', 'r', encoding="utf-8") as f:
                data = f.readlines()
                for line in data:
                    temp_line = line.split()
                    if temp_line[0] == login_user and sha256_crypt.verify(login_pass, temp_line[1]):
                        session['username'] = login_user
                        return redirect(url_for('main'))
        except FileNotFoundError:
            error = 'File Not Found'
            print(error)
        except IndexError:
            error = 'Index Error'
            print(error)
    return render_template('login.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

@app.route('/logout')
def logout():
    """Logout"""
    session["username"] = None
    return redirect('login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration form"""

    if request.method == 'POST':
        register_user = request.form['username']
        register_pass = request.form['password']

        if not register_user:
            error = 'Please enter your Username.'
            print(error)
        elif not register_pass:
            error = 'Please enter your Password.'
            print(error)
        elif not checknotreg(register_user):
            error = 'You are already registered'
            print(error)
        elif not complexity(register_pass):
            error = 'Make your password more complex'
            print(error)
        else:
            with open('passfile', 'a', encoding="utf-8") as f:
                f.write(register_user + " " + sha256_crypt.hash(register_pass) + "\n")
            return redirect(url_for('login'))
    return render_template('register.html', time_now = f"{datetime.datetime.now():%Y%b%d %I:%M %p}")

def checknotreg(register_user: str):
    """Check if user was already registered"""
    check = True
    try:
        with open("passfile", 'r', encoding="utf-8") as f:
            data = f.read()
            for line in data:
                if line[0] == register_user:
                    check = False
    except FileNotFoundError:
        error = 'File Not Found'
        print(error)
    return check

def complexity(register_pass: str):
    """Check complexity of user pass"""
    reg_expression = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    ret_pattern = re.compile(reg_expression)
    check = re.search(ret_pattern, register_pass)

    return check

if __name__ == "__main__":
    app.run(debug=True)
