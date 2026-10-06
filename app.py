from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask App! <=>routing"

@app.route('/greet/<username>')
def greet(username):
    return f"Hello Good Morning, {username}!"

@app.route('/delete/<int:roll>')
def delete_user(roll):
    return redirect(url_for('greet', username='guest'))

@app.route('/calculate', methods=['GET', 'POST'])
@app.route('/calculator', methods=['GET', 'POST'])
def si():
    result = None
    principal = 0.0
    time = 0.0
    rate = 0.0
    total_amount = None

    if request.method == 'POST':
        try:
            principal = float(request.form.get('p', 0) or 0)
            time = float(request.form.get('t', 0) or 0)
            rate = float(request.form.get('r', 0) or 0)
            result = (principal * time * rate) / 100
            total_amount = principal + result
        except (TypeError, ValueError):
            result = 'Invalid input'

    return render_template(
        'index.html',
        result=result,
        p=principal,
        t=time,
        r=rate,
        total_amount=total_amount
    )

if __name__ == '__main__':
    app.run(debug=True, port=3500)