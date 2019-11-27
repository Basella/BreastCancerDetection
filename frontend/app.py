from __init__ import app

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)