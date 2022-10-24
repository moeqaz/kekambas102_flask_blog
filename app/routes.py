from app import app

# Create a route using the @app.route to trigger function based on endpoint
@app.route('/')
def index():
    return 'Hello this is the index route!'


# Add another route
@app.route('/posts')
def posts():
    return 'Hi this is Posts'