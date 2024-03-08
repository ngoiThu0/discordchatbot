from flask import Flask
import os

app = Flask(__name__)

# Your routes and other configurations go here

if __name__ == "__main__":
    # Use the PORT environment variable if available, otherwise use 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Run the Flask app on 0.0.0.0 (all available network interfaces)
    app.run(host="0.0.0.0", port=port)