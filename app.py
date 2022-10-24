# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class and give it a variable name 'app'
app = Flask(__name__)

# Create a route using the @app.route to trigger function based on endpoint
@app.route('/')
def index():
    return 'Hello this is the index route!'


# Run the application 
# if __name__ == '__main__':
#     app.run()

# Add another route
@app.route('/posts')
def posts():
    return 'Posts will eventually be on this page.'