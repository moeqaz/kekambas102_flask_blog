from flask import render_template
from app import app

# Create a route using the @app.route to trigger function based on endpoint
@app.route('/')
def index():
    user_info = {
        'username': 'moeqaz',
        'email': 'usamaqazi@rrr.com'
    }
    return render_template('index.html', user=user_info)


# Add another route
@app.route('/posts')
def posts():
    return 'Hi this is Posts'