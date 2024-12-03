from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Here, you can handle form submission (e.g., save to a database or send email)
    print(f"New message from {name} ({email}): {message}")

    return redirect(url_for('index'))  # Redirect back to home page after form submission

if __name__ == "__main__":
    app.run(debug=True)
