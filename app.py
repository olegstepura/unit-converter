from unit_converter import app, socketio
import os

if __name__ == "__main__":
    # For development only - use gunicorn in production
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    socketio.run(app, host=host, port=port, debug=False, allow_unsafe_werkzeug=True)
