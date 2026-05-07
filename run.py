from app import create_app, db
import webbrowser
from threading import Timer

app = create_app()

# Automatically create database tables if they don't exist
# This ensures Render initializes the PostgreSQL database automatically!
with app.app_context():
    db.create_all()

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Wait 1.5 seconds for the server to spin up, then launch the browser
    Timer(1.5, open_browser).start()
    # Debug=False is important for executables so it doesn't double-load
    app.run(debug=False, port=5000)
