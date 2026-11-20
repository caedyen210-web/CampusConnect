
from flask import Flask, render_template
from routes.api_routes import api_routes
from routes.event_routes import event_routes

app = Flask(__name__)
    
app.register_blueprint(api_routes)
    
app.register_blueprint(event_routes)

@app.route("/")
def index():
 return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
