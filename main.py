from flask import Flask, request, render_template
from flask_restful import Resource, Api

# Initialize server
app = Flask(__name__)
api = Api(app)


@app.route("/") 
def hello(): 
    message = "Hello, World"
    return render_template('index.html',  
                           message=message) 


# Run last
app.run(port=5000, debug = True)