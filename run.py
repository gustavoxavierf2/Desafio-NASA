from flask import Flask

app = Flask(__name__)

from App.router.index import *

if __name__ == '__main__':  
    app.run(debug=True)