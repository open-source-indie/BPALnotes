#imports#
from website import create_app
from flask import Flask


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=False)

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)
    app.run(host = '0.0.0.0', port =5000)

    
#Admin panel
