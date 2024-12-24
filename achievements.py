from flask import Flask, render_template, send_from_directory
import json

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        with open('achievements.json', 'r') as f:
            achievements = json.load(f)
        return render_template('achievements.html', achievements=achievements)

    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory('static', filename)

    return app

def main(): 
    from credit import clear
    import threading
    from waitress import serve

    clear()
    app = create_app()
    flask_thread = threading.Thread(target=serve, args=(app,), kwargs={'host': '0.0.0.0', 'port': 5001})
    flask_thread.start()

    print("Hello World")
    input("Press Enter to exit...")

if __name__ == '__main__':
    main()
