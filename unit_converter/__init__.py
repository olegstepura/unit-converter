from flask import Flask, request, session
from flask_babel import Babel
from flask_socketio import SocketIO
import os
import logging

# Suppress eventlet warnings and errors
os.environ['EVENTLET_HUB'] = 'selects'
os.environ['EVENTLET_SHOW_STACKTRACES'] = 'false'
# Suppress eventlet socket errors
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning, module='eventlet')

# Get the absolute path to the parent directory 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Set template and static folder paths relative to where app is created
app = Flask(
    __name__,
    template_folder=os.path.join(project_root, 'templates'),
    static_folder=os.path.join(project_root, 'static')
)

# Configure i18n
app.config['LANGUAGES'] = {
    'en': 'English',
    'ru': 'Русский',
    'de': 'Deutsch',
    'zh': '中文'
}
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(project_root, 'translations')
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Define locale selector function before initializing Babel
def get_locale():
    # Check if language is set in session
    if 'language' in session:
        return session['language']
    # Try to get from URL parameter
    lang = request.args.get('lang')
    if lang and lang in app.config['LANGUAGES']:
        session['language'] = lang
        return lang
    # Try to get from Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys()) or 'en'

# Initialize Babel - Flask-Babel 4.0.0 uses locale_selector parameter
babel = Babel(app, locale_selector=get_locale)

# Suppress socketio/engineio connection/disconnection errors
logging.getLogger('socketio').setLevel(logging.CRITICAL)
logging.getLogger('engineio').setLevel(logging.CRITICAL)
logging.getLogger('eventlet').setLevel(logging.ERROR)
logging.getLogger('eventlet.wsgi').setLevel(logging.ERROR)
logging.getLogger('werkzeug').setLevel(logging.WARNING)

# Suppress gunicorn verbose logs
logging.getLogger('gunicorn').setLevel(logging.WARNING)
logging.getLogger('gunicorn.error').setLevel(logging.WARNING)
logging.getLogger('gunicorn.access').setLevel(logging.WARNING)

# Suppress urllib3 and other common noisy loggers
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)

# Filter out "Bad file descriptor" and socket shutdown errors
class BadFileDescriptorFilter(logging.Filter):
    def filter(self, record):
        msg = str(record.getMessage())
        # Filter out various forms of these errors
        if 'Bad file descriptor' in msg:
            return False
        if 'socket shutdown error' in msg:
            return False
        if '[Errno 9]' in msg and 'Bad file descriptor' in msg:
            return False
        if 'socket.io' in msg.lower() and ('shutdown' in msg.lower() or 'errno 9' in msg.lower()):
            return False
        return True

bad_fd_filter = BadFileDescriptorFilter()
# Apply filter to all loggers
logging.getLogger().addFilter(bad_fd_filter)
logging.getLogger('socketio').addFilter(bad_fd_filter)
logging.getLogger('engineio').addFilter(bad_fd_filter)
logging.getLogger('eventlet').addFilter(bad_fd_filter)
logging.getLogger('eventlet.wsgi').addFilter(bad_fd_filter)
logging.getLogger('gunicorn.error').addFilter(bad_fd_filter)

# Set root logger to WARNING to suppress INFO and DEBUG messages
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')

# Initialize SocketIO with custom path
socketio = SocketIO(app, cors_allowed_origins="*", logger=False, engineio_logger=False, path="/convert")

# Handle disconnections gracefully
@socketio.on('disconnect')
def handle_disconnect():
    try:
        pass
    except (OSError, IOError) as e:
        # Silently ignore socket errors on disconnect
        if 'Bad file descriptor' not in str(e) and 'Errno 9' not in str(e):
            pass

from unit_converter import route


