from run import app
from flask import render_template

@app.route('/a')
def index():
   return render_template('index.html')