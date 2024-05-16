from flask import Flask, request, render_template, url_for
from flask_restful import Resource, Api
from markupsafe import escape

# Initialize server
app = Flask(__name__)
api = Api(app)


@app.route("/") 
def home_page(): 
    message = "Welcome to my blogs!"
    return render_template('index.html',  
                           message=message) 


@app.route("/blogs/<string:id>") 
def routes_to_blogs(id): 
    return render_template(f'{escape(id)}.html') 


# Run last
app.run(port=5000, debug = True)